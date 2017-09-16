"""
第26行 msg_text=d["cards"][2]["mblog"]["text"] 中的2可能与小偶像的首条微博不符请自行调整。单针对李想而言，[0]是微博置顶，[1]排微博推荐，[2]才是最新微博。
"""
from qqbot.utf8logger import DEBUG
from qqbot.utf8logger import INFO
from qqbot import qqbotsched
import requests
import json
from datetime import datetime
import re
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

@qqbotsched(hour='0-23', minute='0-59/1')
def check_weibo(bot):
    gl = bot.List('group', '389660866')
    if gl is not None:
        for group in gl:
            url="https://m.weibo.cn/api/container/getIndex"
            payload={'type':'uid','value':'5879771257','containerid':'1076035879771257'}       #设置为小偶像的微博地址
            
            r=requests.post(url,data=payload)
            raw_text=r.text
            d=json.loads(raw_text)
            msg_text=d["cards"][2]["mblog"]["text"]
            dr = re.compile(r'<[^>]+>',re.S)
            msg_text = dr.sub('',msg_text)
            msg_id=str(d["cards"][2]["mblog"]["id"])
            now_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(now_time+":"+msg_id)
            f=open("~/.qqbot-tmp/plugins/weibo_msg",'r')      #设置你weibo_msgid存放的目录，推荐放在~/.qqbot-tmp/plugins/
            if(msg_id!=f.read()):
                f=open("~/.qqbot-tmp/plugins/weibo_msg",'w')      #设置你weibo_msgid存放的目录，推荐放在~/.qqbot-tmp/plugins/
                f.write(msg_id)
                bot.SendTo(group,"小偶像发微博啦！"+"\n"+"微博内容："+msg_text)
            f.close()
