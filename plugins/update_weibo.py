
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

def config():    #设置抓取小偶像的键值。可使用chrome的开发者工具或同类型插件，详情见：http://www.nikochan.cc/2017/08/03/Crawlerweibonotloggin/
    value=5879771257
    containerid=1076035879771257
    return value,containerid

def return_msg_text(d,index):
    msg_text=d["cards"][index]["mblog"]["text"]
    dr = re.compile(r'<[^>]+>',re.S)
    msg_text = dr.sub('',msg_text)
    msg_id=str(d["cards"][index]["mblog"]["id"])
    now_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return (msg_text,msg_id)

@qqbotsched(hour='0-23', minute='0-59/1')
def check_weibo(bot):
    gl = bot.List('group', '389660866')
    if gl is not None:
        for group in gl:
            value=config()[0]
            containerid=config()[1]

            url="https://m.weibo.cn/api/container/getIndex"
            payload={'type':'uid','value':value,'containerid':containerid}      
            r=requests.post(url,data=payload)
            raw_text=r.text
            d=json.loads(raw_text)
            msglib=d["cards"]
            if msglib[1]['card_type'] == '9':
                index=1
                msg_text=return_msg_text(d,index)[0]
                msg_id=return_msg_text(d,index)[1]
                print(msg_text)
                print(msg_id)
            else:
                index=2
                msg_text=return_msg_text(d,index)[0]
                msg_id=return_msg_text(d,index)[1]
                print(msg_text)
                print(msg_id)
            now_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(now_time+":",msg_id)
            f=open("/Users/Niko/.qqbot-tmp/plugins/weibo_msg",'r')      #设置你weibo_msgid存放的目录，推荐放在~/.qqbot-tmp/plugins/
            if(msg_id!=f.read()):
                f=open("/Users/Niko/.qqbot-tmp/plugins/weibo_msg",'w')      #设置你weibo_msgid存放的目录，推荐放在~/.qqbot-tmp/plugins/
                f.write(msg_id)
                bot.SendTo(group,"小偶像发微博啦！"+"\n"+"微博内容："+msg_text)
            f.close()
