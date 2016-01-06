#!usr/bin/python
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))

s.send('GET / HTTP/1.1\r\nHOST: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = ''.join(buffer)
head, html = data.split('\r\n\r\n', 1)
print head

with open('sina.html','w') as f:
    f.write(html)

s.close()