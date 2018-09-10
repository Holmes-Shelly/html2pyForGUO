#-*- coding:utf-8 -*-
import requests
import sys
import json
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://ndes.csrc.gov.cn/alappl/home/gongshi2'
last_query = ()

# 获取网页内容
def html_query():
	html_response = requests.get(url).content.decode('utf-8')
	# print type(html_response)
	any_change(html_analyze(html_response))
	return

# 对网页内容进行正则分析的函数，返回一个长度为10的，包含10个title字符串
def html_analyze(content):
	res = r'<span.*?titleshow.*?>(.*?)</span>'
	ans = re.findall(res, content, re.I|re.S|re.M)
	return tuple(ans)

# 与上次查询结果做对比
def any_change(query_result):
	global last_query
	if(query_result != last_query):
		last_query = query_result
		# send email
		send_email(query_result[0])
		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print "something different"
		print query_result[0]
	return

def send_email(msg):
	pass
	return
	
# 网页查询函数，每20s查询一次
def query_cycle():
	while(1):
		html_query()
		time.sleep(60)
	return

# 开始查询	
query_cycle()