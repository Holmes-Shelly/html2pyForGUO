# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="shihao1024@163.com"   #用户名
mail_pass="shihao1992"   #口令

sender = 'shihao1024@163.com'
receivers = 'shihao1024@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('http://ndes.csrc.gov.cn/alappl/home/gongshi', 'plain', 'utf-8')
message['From'] = "shihao<shihao1024@163.com>"
message['To'] =  "guomengdi<marygmd123@163.com>"

subject = '进度跟踪已更新'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print u"邮件发送成功"
except smtplib.SMTPException:
    print u"Error: 无法发送邮件"