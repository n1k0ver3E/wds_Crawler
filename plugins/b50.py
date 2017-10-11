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
import re
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url1="https://wds.modian.com/show_weidashang_pro/8098#1"
url2="https://wds.modian.com/ranking_list?pro_id=8098"
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
r1=requests.get(url1,verify=False,headers=headers)
r2=requests.get(url2,verify=False,headers=headers)

html_doc_1=r1.text
html_doc_2=r2.text
soup1=BS4(html_doc_1,"html.parser")
soup2=BS4(html_doc_2,"html.parser")
global base
base=" "
def onQQMessage(bot, contact, member, content):
    if content == 'wds':
        bot.SendTo(contact, July_wds.start())
    elif content == '排行':
        bot.SendTo(contact,rank.start())
    elif content == 'flag':
        bot.SendTo(contact,flag())
    elif content == '口袋':
        bot.SendTo(contact,koudai())
    elif '@ME' in content:
        bot.SendTo(contact,member.name+"初次见面，请多指教！！")

def flag():
    return("今天还有2名义士立下了追加Flag，希望大家努力让他们早日拔旗～"+"\n"+"① 现在参与人数为【18】人，截止到14日24点整，绫鱼按照集资打卡人数（需单笔不少于2.5）乘以2.5追加，如果集资金额达到【3000】，额外追加【200】。"+"\n"+"② 从集资总额达到【2000】开始，截止到18日，按照集资金额，每增加【32】，残花追投一票，上限【8000元整】。"+"\n"+"大家千万不要放过他们哟～想推有理想！")

def koudai():
    return("脑门儿的口袋提醒：本周口袋48的公社图文社区，有参与开屏活动的投稿，大家记得每日打开app签到领取免费鸡腿，并进去文稿赠送，让我们一起努力为李想拿下本周的开屏奖励！")

def test():
    g = bot.List('group', "456班")[0]
    print (bot.List(g))

@qqbotsched(hour='0-23', minute='0-59', second='0-59/30')
def mytask(bot):
    global base
    url1="https://wds.modian.com/show_weidashang_pro/8098#1"
    r1=requests.get(url1,verify=False,headers=headers)
    html_doc_1=r1.text
    soup1=BS4(html_doc_1,"html.parser")
    gl = bot.List('group', '556592071')
    if gl is not None:
        for group in gl:
            result=return_top()
            if(result != -1):
                bot.SendTo(group,return_ans(result))
        
            
def return_top():
	url1="https://wds.modian.com/show_weidashang_pro/8098#1"
	headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
	temp_array=[]
	r1=requests.get(url1,verify=False,headers=headers)
	html_doc_1=r1.text
	soup=BS4(html_doc_1,"html.parser")
	soup1=soup.li
	result=soup1.find_all("a", attrs={"class": "add-jubao"})[0]
	#print(result)
	comid=result.get('to_comid')
	#print(comid)
	temp_array.append(comid)

	res=soup1.find_all("span","nick")[0].get_text()
	#print(res)
	temp_array.append(res)
	print(temp_array)

	f=open("/Users/Niko/.qqbot-tmp/plugins/b50_msg",'r')

	if(temp_array[0]!=f.read()):
		f=open("/Users/Niko/.qqbot-tmp/plugins/b50_msg",'w')
		f.write(temp_array[0])
		post_name=temp_array[1]
		f.close()
		return (post_name)
	f.close()
	return (-1)


def return_ans(result):
    url1="https://wds.modian.com/show_weidashang_pro/8098#1"
    r1=requests.get(url1,verify=False,headers=headers)
    html_doc_1=r1.text
    soup1=BS4(html_doc_1,"html.parser")

    nick_sup=[]
    money_sup=[]
    rg=soup1.find("div",class_="b").get_text()
    num=int(rg[0:2])
    print(num)
    people=num
    if num>=20:
        num=20
    print (people)
    fond=4000
    res=soup1.find_all("div", class_="mon current")[0].find_all("span")[1].get_text()
    res=res[1:]
    res=float(res.replace(',',""))
    sub=round(fond-res,2)
    if sub<=0:
        sub=0


    for i in range(num):
        nick=soup2.find_all("span","nickname")[i].get_text()
        nick_sup.append(nick)
        money=soup1.find_all("span","nick_sup")[0].get_text()
    for i in range(num):
        if(result==nick_sup[i]):
            print (i)
            return ("刚刚"+result+"聚聚 "+money+"！"+"在聚聚榜上排名第"+str(i+1)+"位！"+"\n"+"wds链接：http://jli.li/I")
        else:
            return ("刚刚"+result+"聚聚 "+money+"！"+"\n"+"现在共有"+str(people)+"个人参与了活动。"+"wds链接：http://jli.li/I")


