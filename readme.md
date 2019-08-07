# 简介
抓取最新的油价信息，包括油价涨跌提醒（默认8小时更新一次数据）

数据源地址： http://www.qiyoujiage.com

# 安装
放入 <config directory>/custom_components/ 目录

# 配置
**Example configuration.yaml:**
```yaml
sensor:
  - platform: oilprice
    name: 最新油价
    region: zhejiang
```


# 前台界面
原始的界面是这样的

![avatar](https://github.com/aalavender/OilPrice/blob/master/2.PNG)

建议采用[markdown-mod](https://github.com/thomasloven/lovelace-markdown-mod )进行展示，效果是这样的

![avatar](https://github.com/aalavender/OilPrice/blob/master/1.PNG)

list-card 的lovelace-ui配置：
```
    cards:
      - content: >
          > ### [[ sensor.zui_xin_you_jie.state ]]

          *[[ sensor.zui_xin_you_jie.attributes.tips ]]*


          > 92#<ha-icon icon="mdi:gas-station"></ha-icon>  <font
          color=#ea4335>[[ sensor.zui_xin_you_jie.attributes.浙江92#汽油 ]]
          </font>&nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  95# <ha-icon
          icon="mdi:gas-station"></ha-icon>  <font color=#fbbc05> [[
          sensor.zui_xin_you_jie.attributes.浙江95#汽油 ]] </font> <p> 98#<ha-icon
          icon="mdi:gas-station"></ha-icon> <font color=#4285f4> [[
          sensor.zui_xin_you_jie.attributes.浙江98#汽油 ]]</font> &nbsp;  &nbsp; 
          &nbsp;  &nbsp;  &nbsp; 0#柴<ha-icon icon="mdi:gas-station"></ha-icon>
          <font color=#34a853> [[ sensor.zui_xin_you_jie.attributes.浙江0#柴油 ]]
          </font>
            
        title: 浙江油价
        type: markdown
```
