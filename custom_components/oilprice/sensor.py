"""
A component which allows you to parse http://www.qiyoujiage.com/zhejiang.shtml get oil price

For more details about this component, please refer to the documentation at
https://github.com/aalavender/OilPrice/

"""
import re
import logging
import asyncio
import voluptuous as vol
import datetime
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from homeassistant.const import (CONF_NAME, CONF_REGION)
from requests import request
from bs4 import BeautifulSoup

__version__ = '0.1.0'
_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['requests', 'beautifulsoup4']

COMPONENT_REPO = 'https://github.com/aalavender/OilPrice/'
SCAN_INTERVAL = datetime.timedelta(hours=8)
ICON = 'mdi:gas-station'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_REGION): cv.string,
})


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    _LOGGER.info("async_setup_platform sensor oilprice")
    async_add_devices([OilPriceSensor(name=config[CONF_NAME], region=config[CONF_REGION])],True)


class OilPriceSensor(Entity):
    def __init__(self, name: str, region: str):
        self._name = name
        self._region = region
        self._state = None
        self._entries = {}

    def update(self):
        _LOGGER.info("sensor oilprice update info from http://www.qiyoujiage.com/")
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }
        response = request('GET', 'http://www.qiyoujiage.com/' + self._region + '.shtml', headers=header)  # 定义头信息发送请求返回response对象
        response.encoding = 'utf-8'   #不写这句会乱码
        soup = BeautifulSoup(response.text, "lxml")
        dls = soup.select("#youjia > dl")
        self._state = soup.select("#youjiaCont > div")[1].contents[0].strip()

        for dl in dls:
            k = re.search("\d+", dl.select('dt')[0].text).group()
            self._entries[k] = dl.select('dd')[0].text
        self._entries["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d')
        self._entries["tips"] = soup.select("#youjiaCont > div:nth-of-type(2) > span")[0].text.strip()  # 油价涨跌信息

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        return self._entries
