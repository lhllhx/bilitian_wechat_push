# 天选中奖自动推送

魔改自项目 https://github.com/paulzzh/BiliGuardsLite  

首先需要在http://sc.ftqq.com/3.version   注册申请SCKEY
然后在./conf/BiliBiliHelper.conf中填写bilibili账号密码 和 sckey

项目首次运行时会自动推送最后一次中奖信息 默认十分钟检测一次

## 环境依赖
|Requirement|
|-------|
|Python 3.6+|
|  rsa    |
|requests |
|configobj|

通常使用 `pip` 工具安装依赖。


## 感谢
 - BilibiliHelper https://github.com/TheWanderingCoel/BiliBiliHelper
 - bilibili-live-tools https://github.com/Dawnnnnnn/bilibili-live-tools
 - 下次一定白嫖 https://live.bilibili.com/164725


# 以下为原原项目Readme

<p align="center"><img width="300px" src="https://i.loli.net/2018/04/20/5ad97bd395912.jpeg"></p>

<p align="center">
<img src="https://img.shields.io/badge/version-0.0.1-green.svg?longCache=true&style=for-the-badge">
<img src="https://img.shields.io/badge/license-GPL%20V3-blue.svg?longCache=true&style=for-the-badge">
</p>


# BiliBiliHelper
B 站直播实用脚本Python版本

## 功能组件

|plugin              |version  |description   |
|--------------------|---------|--------------|
|AsyncioCurl         |19.03.07 |异步的网络请求组件|
|Auth                |19.03.07 |帐号登录组件    |
|Capsule             |19.03.07 |扭蛋机(普通)    |
|Console             |19.03.07 |控制台组件      |
|Coin2Silver         |19.03.07 |硬币换银瓜子组件 |
|Curl                |19.03.17 |非异步的网络请求组件|
|Danmu               |19.03.07 |弹幕监听组件    |
|DailyBag            |19.03.07 |每日礼包领取    |
|Group               |19.03.07 |应援团签到      |
|Guard_Raffle_Handler|19.03.07 |大航海抽奖模块  |
|Heart               |19.04.06 |双端直播间心跳  |
|Silver2Coin         |19.03.07 |银瓜子换硬币    |
|SilverBox           |19.04.11 |免费宝箱领取    |
|Storm_Raffle_Handler|19.03.07 |节奏风暴抽奖模块|
|Task                |19.04.06 |每日任务       |
|Tv_Raffle_Handler   |19.03.31 |小电视抽奖模块 |


## 未完成功能
|待续|
|-------|
| ~~节奏风暴抽奖卡死修复~~ |
| 动态抽奖 |


## 环境依赖
|Requirement|
|-------|
|Python 3.6+|
|aiohttp  |
|  rsa    |
|requests |
|configobj|

通常使用 `pip` 工具安装依赖。


## 使用指南

 1. 下载（克隆）项目代码，初始化项目
```
$ git clone https://github.com/TheWanderingCoel/BiliBiliHelper.git
$ cd BiliBiliHelper
```
 2. 使用 pip 工具进行安装。**如果不了解 PIP 工具的使用，可以直接到 https://github.com/TheWanderingCoel/BiliBiliHelper/releases 下载编译好的程序，解压后跳到第三步。**
```
$ pip install -r requirements.txt
```
 3. 按照[说明](https://github.com/TheWanderingCoel/BiliBiliHelper/blob/master/Doc/Config.md)修改配置文件 `BiliBiliHelper.conf`，只需填写帐号密码即可
 4. 运行测试
```
$ python main.py
```

<p align="center"><img width="680px" src="https://s2.ax1x.com/2019/03/07/kxF8k4.png"></p>


## 部署指南
如果你将 BiliBiliHelper 部署到线上服务器时，则需要配置一个进程监控器来监测 `python main.py` 命令，在它意外退出时自动重启。

通常可以使用以下的方式
 - systemd (推荐)
 - Supervisor
 - screen
 - nohup

## systemd 脚本
```
# /usr/lib/systemd/system/bilibili.service

[Unit]
Description=BiliBiliHelper Manager
Documentation=https://github.com/TheWanderingCoel/BiliBiliHelper
After=network.target

[Service]
ExecStart=/usr/bin/python /path/to/your/BiliBiliHelper/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Supervisor 配置
```
[program:bilibili]
process_name=%(program_name)s
command=python /path/to/your/BiliBiliHelper/main.py
autostart=true
autorestart=true
redirect_stderr=true
```

## 直播间 ID 问题
config 文件中有个 `ROOM_ID` 配置，填写此项可以清空临过期礼物给指定直播间。

通常可以在直播间页面的 url 获取到它
```
http://live.bilibili.com/23058
```

所有直播间号码小于 1000 的直播间为短号，该脚本在每次启动会自动修正，无需关心，


## 感谢
 - BilibiliHelper(php) https://github.com/metowolf/BilibiliHelper
 - blivedm             https://github.com/yjqiang/blivedm
 - bilibili-live-tools https://github.com/yjqiang/bilibili-live-tools
 - bili2.0             https://github.com/yjqiang/bili2.0



## License 许可证

本项目基于 GPL V3 协议发布。

本项目的所有代码文件、配置项，除另有说明外，均基于上述介绍的协议发布，具体请看分支下的 LICENSE。

此处的文字仅用于说明，条款以 LICENSE 文件中的内容为准。
