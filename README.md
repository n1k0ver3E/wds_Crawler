# wds_Crawler
SNH48 bej48 微打赏集资爬虫/微博内容推送的qqbot插件

## 0x00 NEW!!
更新``update_weibo.py`` ——追加新微博检测功能

## 0x01 简介
这是一个基于[qqbot](https://github.com/pandolia/qqbot)对SNH48g的集资情况进行跟踪并实时播报的插件。


``new.py`` 本插件的启动程序

``rank.py`` 可获取该集资链接的排名TOP 20

``July_wds.py`` 是发送定时消息的函数

``update_weibo.py`` 是新微博检测插件

通过每30s进行一次轮询预设好的集资链接，来进行最新集资情况的判断。

## 0x02 功能
* 可定时循环发送指定内容
* 实时监控预设好的集资链接并及时发送最新的集资人信息及数额。
* 回复“flag”可返回flag信息
* 回复“排行”可获得最新的jz排行情况
* 检测最新微博内容并发送新微博提醒和文字内容

## 0x03 使用
1. 在 Python 2.7/3.4+ 下使用，用 pip 安装：``pip install qqbot``

2. 将``/plugins``的全部内容拷贝到``.qqbot-tmp/plugins/``下。再开启新的终端 运行``qq plug new``即可。

3. 在终端输入``qq plug update_weibo`` 运行新微博提醒插件。
3. 其他详细的qqbot使用方法详见[Readme](https://github.com/pandolia/qqbot)

4. 关于新浪微博模拟登陆原理详见[nikochan.cc](http://www.nikochan.cc/2017/08/03/Crawlerweibonotloggin/)

## 0x04 感谢
* [pandolia/qqbot]()

## 0x05 其他
没想到夏天结束了，冬天这么早就开始了。本插件会按照群内需求实时保持更新。

如果有其他意见以及bug欢迎提出来！

*希望各位看到觉得有帮助可以star一下！*

08.23.17

---------
夏天结束了。

我们B50，再见！


*Best wishes to BEJ48 Team E LiXiang.* 

07.29.17
