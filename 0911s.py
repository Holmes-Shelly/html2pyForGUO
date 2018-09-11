#-*- coding:utf-8 -*-
import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://ndes.csrc.gov.cn/alappl/home/volunteerLift?edCde=300009'
last_query = ()
ok_list = [
{'name':'beijingok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofbj/3284/3566/index_887.htm'},
{'name':'tianjinok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicoftj/3284/3566/index_1008.htm'},
{'name':'hebeiok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofheb/3284/3566/index_1030.htm'},
{'name':'shanxiok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofsx/3284/3566/index_1041.htm'},
{'name':'neimengguok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofnmg/3284/3566/index_1052.htm'},
{'name':'liaoningok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofln/3284/3566/index_1063.htm'},
{'name':'jilinok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofjl/3284/3566/index_1074.htm'},
{'name':'heilongjiangok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofhlj/3284/3566/index_1085.htm'},
{'name':'shanghaiok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofsh/3284/3566/index_1239.htm'},
{'name':'jiangsuok', 'url':'http://www.csrc.gov.cn/pub/zjhpublicofjs/3284/3566/index_1228.htm'},
{'name':'beijingok', 'url':''},
{'name':'beijingok', 'url':''},
{'name':'beijingok', 'url':''},
{'name':'beijingok', 'url':''},
{'name':'beijingok', 'url':''},
{'name':'beijingok', 'url':''},
{'name':'beijingok', 'url':''},

]
no_list = [
{'name':'beijingno', 'url':'http://www.csrc.gov.cn/pub/beijing/bjxyzl/bjxzcf'},
{'name':'tianjinno', 'url':'http://www.csrc.gov.cn/pub/tianjin/xzcf/'},
{'name':'hebeino', 'url':'http://www.csrc.gov.cn/pub/hebei/hbxzcf/'},
{'name':'shanxino', 'url':'http://www.csrc.gov.cn/pub/shanxi/xzcf/'},
{'name':'neimengguno', 'url':'http://www.csrc.gov.cn/pub/neimenggu/nmgxzcf/'},
{'name':'liaoningno', 'url':'http://www.csrc.gov.cn/pub/liaoning/lnjxzcf/'},
{'name':'jilinno', 'url':'http://www.csrc.gov.cn/pub/jilin/jlxzcf/'},
{'name':'heilongjiangno', 'url':'http://www.csrc.gov.cn/pub/heilongjiang/hljjxzcf/'},
{'name':'shanghaino', 'url':'http://www.csrc.gov.cn/pub/shanghai/xzcf/'},
{'name':'jiangsuno', 'url':'http://www.csrc.gov.cn/pub/jiangsu/jsxzcf/'},
{'name':'beijingno', 'url':''},
{'name':'beijingno', 'url':''},
{'name':'beijingno', 'url':''},
{'name':'beijingno', 'url':''},
{'name':'beijingno', 'url':''},
{'name':'beijingno', 'url':''},

]

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
	receivers = 'marygmd123@163.com'  # 接收邮件

	message = MIMEText('http://ndes.csrc.gov.cn/alappl/home/gongshi'+'\n'+'\n'.join(msg_tuple), 'plain', 'utf-8')
	message['From'] = "shihao<shihao1024@163.com>"
	message['To'] = "guomengdi<marygmd123@163.com>"

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