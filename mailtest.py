#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
	
def send_email():
	# 第三方 SMTP 服务
	mail_host="smtp.163.com"  #设置服务器
	mail_user="shihao1024@163.com"   #用户名
	mail_pass="shihao1992"   #口令

	sender = 'shihao1024@163.com'
	receivers = ['shihao1024@163.com', 'shihao06@gmail.com']  # 接收邮件
	subject = "csrc.gov.cn: 2 important."
	email_content = 'http://ndes.csrc.gov.cn/alappl/home/gongshi'
	
	message = MIMEText(email_content, 'plain', 'utf-8')
	message['From'] = "shihao<shihao1024@163.com>"
	message['To'] =  "guomengdi<marygmd123@163.com>"
	message['Subject'] = Header(subject)

	try:
		smtpObj = smtplib.SMTP_SSL()
		smtpObj.connect(mail_host, 465)
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "send in 465"
		smtpObj_ = smtplib.SMTP()
		smtpObj_.connect(mail_host, 25)
		smtpObj_.login(mail_user,mail_pass)
		smtpObj_.sendmail(sender, receivers, message.as_string())
		print "send in 25"
	except:
		print "send unsuccessfully"
	return

send_email()
