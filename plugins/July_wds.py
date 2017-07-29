def start():
	from bs4 import BeautifulSoup as BS4
	import requests
	import datetime
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

	now=datetime.datetime.now()
	then=datetime.datetime(2017,7,29)
	day=(then-now).days+1

	url1="https://wds.modian.com/show_weidashang_pro/5329#1"
	url2="https://wds.modian.com/ranking_list?pro_id=5329"
	headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

	r=requests.get(url1,verify=False,headers=headers)
	html_doc=r.text
	soup=BS4(html_doc,"html.parser")
	res=soup.find_all("div", class_="mon current")[0].find_all("span")[1].get_text()
	return ("本次活动一共贡献了"+res+"."+"\n"+"在最后的"+str(day)+"天里我们一起创造奇迹吧！"+"\n"+"微打赏地址：http://jli.li/I"+"\n"+"淘宝地址：http://jli.li/J  可信用卡可花呗支付")

	#nick=soup.find_all("span","nick")[0].get_text()
	#nick_sup=soup.find_all("span","nick_sup")[0].get_text()
	#print(nick,nick_sup)

	#nick_rank=
	#rg=soup.find("div",class_="b")
	#print (rg)
if __name__ == '__main__':
	start()
