#!usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = raw_input('From eamil: ')
password = raw_input('Password: ')
smtp_server = raw_input('SMTP server: ')
to_addr = raw_input('To eamil: ')

my_msg = MIMEMultipart()
my_msg['From'] = from_addr
my_msg['Subject'] = 'Test from Python'
my_msg['To'] = to_addr
my_msg['Date'] = formatdate(localtime=True)
my_msg.attach(msg)

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], my_msg.as_string())
server.quit()