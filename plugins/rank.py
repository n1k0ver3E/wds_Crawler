def start():
	import requests
	from bs4 import BeautifulSoup as BS4
	import requests
	import datetime
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	url1="https://wds.modian.com/show_weidashang_pro/5329#1"
	url2="https://wds.modian.com/ranking_list?pro_id=5329"
	headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
	r1=requests.get(url1,verify=False,headers=headers)
	r2=requests.get(url2,verify=False,headers=headers)
	i=0
	result="*******BEJ48-李想7月应援*******"+'\n'
	html_doc_1=r1.text
	html_doc_2=r2.text
	soup1=BS4(html_doc_1,"html.parser")
	soup2=BS4(html_doc_2,"html.parser")

	nick_sup=[]
	money_sup=[]
	rg=soup1.find("div",class_="b").get_text()
	num=int(rg[0:3])

	for i in range(num):
		money=soup2.find_all("span","money")[i].get_text()
		nick=soup2.find_all("span","nickname")[i].get_text()
		nick_sup.append(nick)
		money_sup.append(money)

	for i in range(num):
		result=result+"第"+str(i+1)+"位："+nick_sup[i]+ money_sup[i]+'\n'
	print(result)	
	return result

if __name__ == '__main__':
	start() 
