#-*- coding:utf-8 -*-
import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://ndes.csrc.gov.cn/alappl/home/volunteerLift?edCde=300009'
last_query = ()

# 获取网页内容
def html_query():
	html_response = requests.get(url).content.decode('utf-8')
	any_change(html_analyze(html_response))
	return

# 对网页内容进行正则分析的函数，返回一个长度为10的，包含10个title字符串
def html_analyze(content):
	res = r'<.*?titleshow.*?>(.*?)<.*?>'
	ans = re.findall(res, content, re.I|re.S|re.M)
	# print len(ans)
	return tuple(ans)

# 与上次查询结果做对比
def any_change(query_result):
	global last_query
	if(query_result != last_query):
		diff_tuple = tuple(set(query_result).difference(set(last_query)))
		last_query = query_result
		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print len(diff_tuple), " messages are updated"
		# send email
		send_email(diff_tuple)
	return

def send_email(msg_tuple):
	# 第三方 SMTP 服务
	mail_host="smtp.163.com"  #设置服务器
	mail_user="shihao1024@163.com"   #用户名
	mail_pass="shihao1992"   #口令

	sender = 'shihao1024@163.com'
	receivers = 'shihao1024@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

	message = MIMEText('http://ndes.csrc.gov.cn/alappl/home/gongshi'+'\n'+'\n'.join(msg_tuple), 'plain', 'utf-8')
	message['From'] = "shihao<shihao1024@163.com>"
	message['To'] =  "guomengdi<marygmd123@163.com>"

	subject = str(len(msg_tuple))+" messages are updated"
	message['Subject'] = Header(subject)

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "send successfully"
	except smtplib.SMTPException:
		print "send unsuccessfully"
	return
	
# 网页查询函数，每20s查询一次
def query_cycle():
	while(1):
		html_query()
		time.sleep(600)
	return

# 开始查询	
query_cycle()