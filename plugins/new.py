import July_wds
import check
import rank
from qqbot.utf8logger import DEBUG
from qqbot import qqbotsched
import requests
import wds_check
from bs4 import BeautifulSoup as BS4
import requests
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url1="https://wds.modian.com/show_weidashang_pro/5329#1"  #目标页面
url2="https://wds.modian.com/ranking_list?pro_id=5329"    #目标页面聚聚榜
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
r1=requests.get(url1,verify=False,headers=headers)  
r2=requests.get(url2,verify=False,headers=headers)

html_doc_1=r1.text
html_doc_2=r2.text
soup1=BS4(html_doc_1,"html.parser")
soup2=BS4(html_doc_2,"html.parser")
global base
base=" "
def onQQMessage(bot, contact, member, content):   #发送消息的回调函数
    if content == 'wds':
        bot.SendTo(contact, July_wds.start())
    elif content == '排行':
        bot.SendTo(contact,rank.start())
    elif '@ME' in content:
        bot.SendTo(contact,member.name+"初次见面，请多指教！！")

@qqbotsched(hour='0-23', minute='0-59/1')   #定时函数 每分钟刷新 装饰器相关编写规则请参考qqbot
def mytask(bot):  #jz信息实时更新
    global base
    url1="https://wds.modian.com/show_weidashang_pro/5329#1"
    r1=requests.get(url1,verify=False,headers=headers)
    html_doc_1=r1.text
    soup1=BS4(html_doc_1,"html.parser")
    gl = bot.List('group', '556592071')
    if gl is not None:
        for group in gl:
            result=return_top()
            print ("首位"+result)
            if (result!=base):
                print("before:"+base)
                base=result
                print("after:"+base)
                bot.SendTo(group,return_ans(result))
            else:
                print("equal_before:"+base)
                print("equal_after:"+base)
def return_top():   #获取最新jz用户的ID
    url1="https://wds.modian.com/show_weidashang_pro/5329#1"
    r1=requests.get(url1,verify=False,headers=headers)
    html_doc_1=r1.text
    soup1=BS4(html_doc_1,"html.parser")
    res=soup1.find_all("span","nick")[0].get_text()
    return res

def return_ans(result):  #结果判断
    url1="https://wds.modian.com/show_weidashang_pro/5329#1"
    r1=requests.get(url1,verify=False,headers=headers)
    html_doc_1=r1.text
    soup1=BS4(html_doc_1,"html.parser")

    nick_sup=[]
    money_sup=[]
    rg=soup1.find("div",class_="b").get_text()
    num=int(rg[0:3])
    fond=2500
    res=soup1.find_all("div", class_="mon current")[0].find_all("span")[1].get_text()
    res=res[1:]
    res=float(res.replace(',',""))
    sub=round(fond-res,2)


    for i in range(num):
        nick=soup2.find_all("span","nickname")[i].get_text()
        nick_sup.append(nick)
        money=soup1.find_all("span","nick_sup")[0].get_text()
    for i in range(num):
        if(result==nick_sup[i]):
            return ("刚刚"+result+"聚聚 "+money+"！"+"在聚聚榜上排名第"+str(i+1)+"位！"+"\n"+"现在共有"+str(num)+"个人参与了活动。"+"\n"+"距离今日集资目标【￥"+str(fond)+"】还差【￥"+str(sub)+ "】\n"+"在最后的这段日子里，我们再坚持一下！"+"\n"+"wds链接：https://wds.modian.com/show_weidashang_pro/5329#1")

@qqbotsched(hour='8-23', minute='0-59/30')#定时消息发送
def mytask2(bot):
    gl = bot.List('group', '556592071')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, July_wds.start()) 
