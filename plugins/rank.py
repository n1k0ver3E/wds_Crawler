import requests
from qqbot.utf8logger import DEBUG
from qqbot import qqbotsched
from bs4 import BeautifulSoup as BS4
import requests
import datetime
import re
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import b50

def main():
    soup=b50.crawel_jujurank_url()
    res=[]
    results=soup.find_all("li","line1px")
    for result in results:
        res.append(result)
    length=int(b50.return_support_num())
    if length>=20:
        length=20
    rank=[[] for i in range(length)]
    for i in range(length):
        for link in res[i].find_all('a'):
            user_id = re.sub('[^0-9.]',"",link.get("href"))
            rank[i].append(user_id)

        user_name=res[i].find_all('span','nickname')[0].get_text()
        rank[i].append(user_name)

        user_money=res[i].find_all('span','money')[0].get_text()
        user_money = re.sub('[^0-9.]',"",user_money)
        rank[i].append(user_money)
    return rank    
