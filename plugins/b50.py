import requests
from qqbot.utf8logger import DEBUG
from qqbot import qqbotsched
from bs4 import BeautifulSoup as BS4
import requests
import datetime
import re
import time
import rank
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#主页爬虫
def crawel_wdsmain_url():
    url2="https://wds.modian.com/show_weidashang_pro/8098#1"
    headers={'Accepat':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    r2=requests.get(url2,verify=False,headers=headers)
    html_doc_2=r2.text
    soup=BS4(html_doc_2,"html.parser")
    return soup

#聚聚集资爬虫
def crawel_wds_url():
    url="https://wds.modian.com/ajax/comment_list"
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    payload={'page':'1', 'post_id':'17190','pro_id':'8098'}
    r1=requests.post(url,data=payload, headers=headers)
    raw_text=r1.text
    html_doc_1=str(json.loads(raw_text)['data'])
    soup=BS4(html_doc_1,"html.parser")
    return soup

#聚聚榜爬虫
def crawel_jujurank_url():
    url2="https://wds.modian.com/ranking_list?pro_id=8098"
    headers={'Accepat':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    r2=requests.get(url2,verify=False,headers=headers)
    html_doc_2=r2.text
    soup=BS4(html_doc_2,"html.parser")
    return soup

def onQQMessage(bot, contact, member, content):
    gl = bot.List('group', '556592071')
    if gl is not None:
        for group in gl:
            if content == 'b50' :
                bot.SendTo(group, Ontime())
            elif content == 'B50' :
                bot.SendTo(group, Ontime())
            elif content == 'flag':
                bot.SendTo(group,flag())
            elif content == '口袋':
                bot.SendTo(group,koudai())
            elif '@ME' in content:
                bot.SendTo(group,member.name+"初次见面，请多指教！！")

def Ontime():
    money=return_total_money()
    support_num=return_support_num()
    return("**脑门儿的集资播报：**"+"\n"+"当前活动已筹："+money+"元"+"\n"+"参与人数："+support_num+"\n"+"wds链接：http://jli.li/I"+"\n"+"**B50就要到了,行行好吧！**")

def flag():
    return("今天还有2名义士立下了追加Flag，希望大家努力让他们早日拔旗～"+"\n"+"① 现在参与人数为【18】人，截止到14日24点整，绫鱼按照集资打卡人数（需单笔不少于2.5）乘以2.5追加，如果集资金额达到【3000】，额外追加【200】。"+"\n"+"② 从集资总额达到【2000】开始，截止到18日，按照集资金额，每增加【32】，残花追投一票，上限【8000元整】。"+"\n"+"大家千万不要放过他们哟～想推有理想！")

def koudai():
    return("脑门儿的口袋提醒：本周口袋48的公社图文社区，有参与开屏活动的投稿，大家记得每日打开app签到领取免费鸡腿，并进去文稿赠送，让我们一起努力为李想拿下本周的开屏奖励！")

#定时任务
@qqbotsched(hour='9-23/4')
def b50xingxinghao(bot):
    money=return_total_money()
    post_text="B50就要到了，不来打个卡么？"+"\n"+"当前活动已筹："+money+"元"+"\n"+"wds链接：http://jli.li/I"
    gl = bot.List('group', '556592071')
    if gl is not None:
        for group in gl:
            bot.SendTo(group,post_text)
#Main
@qqbotsched(hour='0-23', minute='0-59', second='0-59/30')
def mytask(bot):
    gl = bot.List('group', '556592071')
    if gl is not None:
        for group in gl:
            result=return_top()
            print("Status：",result)
            if(result != -1):
                bot.SendTo(group,return_ans(result[0],result[1]))
        
            
def return_top():
    temp_array=[]
    soup=crawel_wds_url()
    soup1=soup.li
    result=soup1.find_all("a", attrs={"class": "add-jubao"})[0]
    comid=result.get('to_comid')   #交易ID
    temp_array.append(comid)
    userid=result.get('to_user')    #用户ID
    temp_array.append(userid)
    res=soup1.find_all("span","nick")[0].get_text()    #用户名
    temp_array.append(res)
    print(temp_array)

    f=open("/Users/Niko/.qqbot-tmp/plugins/b50_msg",'r')

    if(temp_array[0]!=f.read()):
        f=open("/Users/Niko/.qqbot-tmp/plugins/b50_msg",'w')
#       f=open("/Users/Niko/.qqbot-tmp/plugins/b50_msg",'w')
        f.write(temp_array[0])
        post_id=temp_array[1]
        post_name=temp_array[2]
        f.close()
        return (post_name,post_id)
    f.close()
    return (-1)

def return_ans(username,userid):
    money = str(return_user_support_money())
    ranking = str(return_user_ranking(userid))
    total = str(return_total_money())
    support_num = str(return_support_num())
    print("ranking",str(ranking),ranking)
    if ranking !='-1':
        return("刚刚 "+username+" 聚聚 "+"在【第四届金曲大赏集资2.0】活动中"+money+"！"+"\n"+"在聚聚榜上排名第"+ranking+"位!"+"\n"+"参与人数："+support_num+"\n"+"活动累计："+total+"元"+"\n"+"wds链接：http://jli.li/I")
    else:
        return("刚刚 "+username+" 聚聚 "+"在【第四届金曲大赏集资2.0】活动中"+money+"！"+"\n"+"参与人数："+support_num+"\n"+"活动累计："+total+"元"+"\n"+"wds链接：http://jli.li/I")

def return_user_ranking(userid):
    userId=int(userid)
    ranking=rank.main()
    #num=int(return_support_num())
    num=20
    for i in range(num):
        rankId=int(ranking[i][0])
        print("userId:", userId)
        print("rankId:", rankId)
        if(userId == rankId):
            return i+1
        else:
            return -1

def return_user_support_money():
    soup=crawel_wds_url()
    money=soup.find_all("span","nick_sup")[0].get_text()
    return money

def return_support_num():
    soup=crawel_wdsmain_url()
    support_text=soup.find("div",class_="b").get_text()
    support_num = re.sub('[^0-9.]',"",support_text)
    return support_num

def return_total_money():
    soup=crawel_wdsmain_url()
    total=soup.find_all("div", class_="mon current")[0].find_all("span")[1].get_text()
    total_num = re.sub('[^a-zA-Z0-9.]',"",total)
    return total_num
