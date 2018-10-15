#-*- coding:utf-8 -*-
import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://www.csrc.gov.cn/pub/'

url_list = [
{'name':'beijing', 
'ok_url':'zjhpublicofbj/3284/3566/index_887.htm', 
'no_url':'beijing/bjxyzl/bjxzcf',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'hebei', 
'ok_url':'zjhpublicofheb/3284/3566/index_1030.htm', 
'no_url':'hebei/hbxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'shanxi', 
'ok_url':'zjhpublicofsx/3284/3566/index_1041.htm', 
'no_url':'shanxi/xzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'liaoning', 
'ok_url':'zjhpublicofln/3284/3566/index_1063.htm', 
'no_url':'liaoning/lnjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'jilin', 
'ok_url':'zjhpublicofjl/3284/3566/index_1074.htm', 
'no_url':'jilin/jlxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'heilongjiang', 
'ok_url':'zjhpublicofhlj/3284/3566/index_1085.htm', 
'no_url':'heilongjiang/hljjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'shanghai', 
'ok_url':'zjhpublicofsh/3284/3566/index_1239.htm', 
'no_url':'shanghai/xzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'jiangsu', 
'ok_url':'zjhpublicofjs/3284/3566/index_1228.htm', 
'no_url':'jiangsu/jsxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'zhejiang', 
'ok_url':'zjhpublicofzj/3284/3566/index_1096.htm', 
'no_url':'zhejiang/zjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'anhui', 
'ok_url':'zjhpublicofah/3284/3566/index_1019.htm', 
'no_url':'anhui/ahxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'fujian', 
'ok_url':'zjhpublicoffj/3284/3566/index_1129.htm', 
'no_url':'fujian/fjjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'shandong', 
'ok_url':'zjhpublicofsd/3284/3566/index_997.htm', 
'no_url':'shandong/sdxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'henan', 
'ok_url':'zjhpublicofhen/3284/3566/index_986.htm', 
'no_url':'henan/hnxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'hubei', 
'ok_url':'zjhpublicofhb/3284/3566/index_942.htm', 
'no_url':'hubei/hbxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'hunan', 
'ok_url':'zjhpublicofhn/3284/3566/index_953.htm', 
'no_url':'hunan/hnxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'guangdong', 
'ok_url':'zjhpublicofgd/3284/3566/index_832.htm', 
'no_url':'guangdong/xzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'chongqing', 
'ok_url':'zjhpublicofcq/3284/3566/index_898.htm', 
'no_url':'chongqing/cqjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'sichuan', 
'ok_url':'zjhpublicofsc/3284/3566/index_1173.htm', 
'no_url':'sichuan/scxzcf/',
'ok_last_query':(),
'no_last_query':(),
},

{'name':'shenzhen', 
'ok_url':'zjhpublicofsz/3284/3566/index_876.htm', 
'no_url':'shenzhen/xzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'dalian', 
'ok_url':'zjhpublicofdl/3284/3566/index_1250.htm', 
'no_url':'dalian/dlxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'ningbo', 
'ok_url':'zjhpublicofnb/3284/3566/index_1107.htm', 
'no_url':'ningbo/nbxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'xiamen', 
'ok_url':'zjhpublicofxm/3284/3566/index_1151.htm', 
'no_url':'xiamen/xmxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'qingdao', 
'ok_url':'zjhpublicofqd/3284/3566/index_975.htm', 
'no_url':'qingdao/xzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'shaanxi', 
'ok_url':'zjhpublicofsax/3284/3566/index_1217.htm', 
'no_url':'',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'guangxi', 
'ok_url':'zjhpublicofgx/3284/3566/index_1140.htm', 
'no_url':'',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'ningxia', 
'ok_url':'zjhpublicofnx/3284/3566/index_920.htm', 
'no_url':'',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'gansu', 
'ok_url':'zjhpublicofgs/3284/3566/index_1118.htm', 
'no_url':'',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'yunnan', 
'ok_url':'zjhpublicofyn/3284/3566/index_1195.htm', 
'no_url':'',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'tianjin', 
'ok_url':'zjhpublicoftj/3284/3566/index_1008.htm', 
# 'no_url':'tianjin/xzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'neimenggu', 
'ok_url':'zjhpublicofnmg/3284/3566/index_1052.htm', 
# 'no_url':'neimenggu/nmgxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'guizhou', 
'ok_url':'zjhpublicofgz/3284/3566/index_1184.htm', 
# 'no_url':'guizhou/gzxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'xizang', 
'ok_url':'zjhpublicofxz/3284/3566/index_1206.htm', 
# 'no_url':'xizang/xzxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'qinghai', 
'ok_url':'zjhpublicofqh/3284/3566/index_931.htm', 
# 'no_url':'qinghai/qhxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'xinjiang', 
'ok_url':'zjhpublicofxj/3284/3566/index_909.htm', 
# 'no_url':'xinjiang/xjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'hainan', 
'ok_url':'zjhpublicofhan/3284/3566/index_1162.htm', 
# 'no_url':'hainan/hnjxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
{'name':'jiangxi', 
'ok_url':'zjhpublicofjx/3284/3566/index_964.htm', 
# 'no_url':'jiangxi/jxxzcf/',
'ok_last_query':(),
'no_last_query':(),
},
]

# 获取审批网页内容
def ok_html_query():
	for province_index in range(len(url_list)):
		# 获取网页信息
		ok_html_response = requests.get(url + url_list[province_index]['ok_url']).content.decode('utf-8')
		ok_this_query = ok_html_analyze(ok_html_response)
		# get update
		ok_diff_tuple = tuple(set(ok_this_query).difference(set(url_list[province_index]['ok_last_query'])))
		if len(ok_diff_tuple) & len(url_list[province_index]['ok_last_query']):
			print "detect change in area_ok"
			file_write('ok_last_query is')
			file_write('\n'.join(url_list[province_index]['ok_last_query']))
			file_write('ok_this_query is')
			file_write('\n'.join(ok_this_query))
			file_write('ok_diff_tuple is')
			file_write('\n'.join(ok_diff_tuple))
			# 发送邮件
			send_email(ok_diff_tuple, url_list[province_index]['ok_url'])
		url_list[province_index]['ok_last_query'] = ok_this_query
		time.sleep(120)
	return
	
# 获取惩罚网页内容
def no_html_query():
	for province_index in range(len(url_list)-13):
		# 获取网页信息
		no_html_response = requests.get(url + url_list[province_index]['no_url']).content.decode('utf-8')
		no_this_query = no_html_analyze(no_html_response)
		# get update
		no_diff_tuple = tuple(set(no_this_query).difference(set(url_list[province_index]['no_last_query'])))
		if len(no_diff_tuple) & len(url_list[province_index]['no_last_query']):
			print "detect change in area_no"
			file_write('no_last_query is')
			file_write('\n'.join(url_list[province_index]['no_last_query']))
			file_write('no_this_query is')
			file_write('\n'.join(no_this_query))
			file_write('no_diff_tuple is')
			file_write('\n'.join(no_diff_tuple))
			# 发送邮件
			send_email(no_diff_tuple, url_list[province_index]['no_url'])
		url_list[province_index]['no_last_query'] = no_this_query
		time.sleep(120)
	return

# 对审批网页内容进行正则分析的函数
def ok_html_analyze(content):
	res = r'<.*?blank.*?displayTip\((\d+).*?>(.*?)<.*?>'
	ans0 = re.findall(res, content, re.I|re.S|re.M)
	ans = []
	for re_tuple in ans0:
		ans.append(''.join(re_tuple))
	# file_write('\n'.join(ans))
	# file_write('\n')
	return tuple(ans)

# 对惩罚网页内容进行正则分析的函数	
def no_html_analyze(content):
	res = r'<.*?_(\d+)\.htm.*?blank.*?>(.*?)<.*?>'
	ans0 = re.findall(res, content, re.I|re.S|re.M)
	ans = []
	for re_tuple in ans0:
		ans.append(''.join(re_tuple))
	# file_write('\n'.join(ans))
	# file_write('\n')
	return tuple(ans)

def send_email(msg_tuple, province_url):
	# 第三方 SMTP 服务
	mail_host="smtp.163.com"  #设置服务器
	mail_user="shihao1024@163.com"   #用户名
	mail_pass="shihao1992"   #口令

	sender = 'shihao1024@163.com'
	receivers = ['marygmd123@163.com', 'shihao1024@163.com']  # 接收邮件

	message = MIMEText(url+province_url+'\n'+'\n'.join(msg_tuple), 'plain', 'utf-8')
	message['From'] = "shihao<shihao1024@163.com>"
	message['To'] = "guomengdi<marygmd123@163.com>"

	subject = str(len(msg_tuple))+" message update"
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
	
# 网页查询函数
def query_cycle():
	cycle_time = 0
	while(1):
		ok_html_query()
		no_html_query()
		cycle_time += 1
		print cycle_time
	return

def file_write(content):
	f = open('test0918.txt', 'a')
	f.write(content.encode('utf-8'))
	f.write('\n')
	f.close
	return
	
# 开始查询	
query_cycle()