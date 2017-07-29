# wds_Crawler
snh48/bej48 微打赏集资 爬虫


##0x00 简介
这是一个基于[qqbot](https://github.com/pandolia/qqbot)对SNH48g的集资情况进行跟踪并实时播报的插件。


``new.py`` 本插件的启动程序

``rank.py`` 可获取该集资链接的排名TOP 20

``July_wds.py`` 是发送定时消息的函数

通过每30s进行一次轮询预设好的集资链接，来判断
##0x01 功能
* 可定时循环发送指定内容
* 实时监控预设好的集资链接并及时发送最新的集资人信息及数额。
* 回复“flag”可返回flag信息
* 回复“排行”可获得最新的jz排行情况

##0x02 使用
1. 在 Python 2.7/3.4+ 下使用，用 pip 安装：``pip install qqbot``

2. 将``/plugins``的全部内容拷贝到``.qqbot-tmp/plugins/``下。再开启新的终端 运行 qq plug new 即可。
3. 其他详细的qqbot使用方法详见[Readme](https://github.com/pandolia/qqbot).

##0x03 感谢
* [pandolia/qqbot]()

