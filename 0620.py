#-*- coding:utf-8 -*-
import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://neris.csrc.gov.cn/alappl/home/volunteerLift.do'
res = ur'<.*?titleshow.*?>(.*?)<.*?>'
key_jj = ur'基金'
key_zq = ur'.*?证券.*?《.*?基金募集.*?'
last_query = []

# main function
def html_query():
	web_items = []
	headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8,lb;q=0.7',
	'Cache-Control': 'max-age=0',
	'Content-Length': '33',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie': 'JSESSIONID=BE162D500FD8CCF5CB80EAA4C1D2F415',
	'Host': 'neris.csrc.gov.cn',
	'Origin': 'http://neris.csrc.gov.cn',
	'Proxy-Connection': 'keep-alive',
	'Referer': 'http://neris.csrc.gov.cn/alappl/home/volunteerLift.do',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
	}
	for page in range(3):
		data = 'edCde=300009&pageNo={}&pageSize=10'.format(str(page+1))
		try:
			web_resp = requests.post(url, data = data, headers = headers).content.decode('utf-8')
		except:
			print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "404 Not Found.")
			
		page_items = re.findall(res, web_resp, re.I|re.S|re.M)
		if(len(page_items) < 10):
			file_write(web_resp)
			print("Interesting.")
			
		for item in page_items:
			web_items.append(item)
		time.sleep(2)
	
	diff_tuple = tuple(set(web_items).difference(set(last_query)))
	if len(diff_tuple):
		key_query = find_key(diff_tuple)
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), len(diff_tuple), "updated.")
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), len(key_query), "important.")
		send_tg(diff_tuple, key_query)
		send_email(diff_tuple, key_query)
		for content_index in range(len(last_query)):
			last_query.pop(-1)
		for content in web_items:
			last_query.append(content)
	return
	
def send_email(html_tuple, msg_tuple):
	
	mail_host="smtp.163.com"  
	mail_user="shihao1024@163.com"   
	mail_pass="shihao1992"  

	sender = 'shihao1024@163.com'
	receivers = ['marygmd123@163.com', 'shihao1024@163.com']
	subject = str(len(html_tuple))+" updated, "+str(len(msg_tuple))+" important."
	email_content = ''
	content_row = 0
	for content in msg_tuple:
		content_row += 1
		email_content = email_content + '\n' + str(content_row) + '. ' + content
	
	message = MIMEText(email_content, 'plain', 'utf-8')
	message['From'] = "shihao<shihao1024@163.com>"
	message['To'] =  "guomengdi<marygmd123@163.com>"
	message['Subject'] = Header(subject)

	try:
		smtpObj = smtplib.SMTP_SSL()
		smtpObj.connect(mail_host, 465)
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
	except smtplib.SMTPException:
		print("send unsuccessfully.")
	return
	
def send_tg(html_tuple, msg_tuple):
	TOKEN = "33637785666:AAHRW-gz-CeKkSGbP_xKubcau0dO28ffBYc"
	url = "https://api.telegram.org/bot{}/".format(TOKEN[2:])
	content = str(len(html_tuple))+" updated, "+str(len(msg_tuple))+" important."

	print(content)
	try:
		requests.get(url + "sendMessage?chat_id=-1001366507371&text={}".format(content.encode('utf-8')))
	except:
		print("tg send unsuccessfully.")
	return
	
def find_key(diff_tuple):
	key_query = []
	for query_content in diff_tuple:
		if re.search(key_jj, query_content):
			if re.match(key_zq, query_content):
				print("zhengquan in jijin.")
				key_query.append(query_content)
		else:
			key_query.append(query_content)
			print("find other thing.")

	return tuple(key_query)
	
def file_write(content):
	f = open('0620.txt', 'a')
	f.write(content.encode('utf-8'))
	f.write('\n')
	f.close
	return
	
def query_cycle():
	while(1):
		time_hour = int(time.strftime('%H',time.localtime(time.time())))
		time_day = int(time.strftime('%w',time.localtime(time.time())))
		if time_hour == 22:
			time_delay = 36000
		elif time_day == 0 or time_day == 6:
			time_delay = 3600
		elif time_hour == 12 or time_hour == 18:
			time_delay = 600
		else:
			time_delay = 3600

		try:
			print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
			html_query()
		except requests.exceptions.ConnectionError as ErrorAlert:
			print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
			print(ErrorAlert)
		time.sleep(time_delay)
	return

query_cycle()
