#-*- coding:utf-8 -*-
import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://ndes.csrc.gov.cn/alappl/home/volunteerLift?edCde=300009'
last_query = ()
key_word = u'基金募集申请'

# main function
def html_query():
	html_response = requests.get(url).content.decode('utf-8')
	this_query = html_analyze(html_response)
	
	global last_query
	diff_tuple = tuple(set(this_query).difference(set(last_query)))
	if len(diff_tuple) and len(last_query):
		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), len(diff_tuple), "updated."
		key_query = find_key(diff_tuple)
		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), len(key_query), "important."
		send_tg(diff_tuple, key_query)
		send_email(diff_tuple, key_query)
	last_query = this_query
	return

def html_analyze(content):
	res = r'<.*?titleshow.*?>(.*?)<.*?>'
	ans = re.findall(res, content, re.I|re.S|re.M)
	return tuple(ans)
	
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
		print "send unsuccessfully"
	return
	
def send_tg(html_tuple, msg_tuple):
	TOKEN = "33637785666:AAHRW-gz-CeKkSGbP_xKubcau0dO28ffBYc"
	url = "https://api.telegram.org/bot{}/".format(TOKEN[2:])
	content = str(len(html_tuple))+" updated, "+str(len(msg_tuple))+" important."

	try:
		requests.get(url + "sendMessage?chat_id=-1001366507371&text={}".format(content.encode('utf-8')))
	except:
		print "tg send unsuccessfully"
	return
	
def find_key(diff_tuple):
	key_query = []
	for query_content in diff_tuple:
		if not re.search(key_word, query_content):
			key_query.append(query_content)
			# print 'find', type(query_content)
	return tuple(key_query)
	
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
			print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			html_query()
		except requests.exceptions.ConnectionError, ErrorAlert:
			print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			print ErrorAlert
		time.sleep(time_delay)
	return

query_cycle()
