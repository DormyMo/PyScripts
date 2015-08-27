#coding:utf8
'''
@author modm
http://www.7mdm.com
'''
import requests
import urllib2
import string
import random
import uuid
import time
import re
import base64
from lxml import etree
proxyList=[{'http': '23.23.204.213:80'}, {'http': '64.186.47.179:8080'}, {'http': '162.248.53.68:10016'}, {'http': '91.121.171.119:4444'}, {'http': '212.82.126.32:80'}, {'http': '91.121.103.144:8080'}, {'http': '59.127.178.95:8888'}, {'http': '62.201.200.5:80'}, {'http': '78.29.12.253:3128'}, {'http': '54.207.49.14:80'}, {'http': '15.126.205.75:8080'}, {'http': '119.81.99.131:80'}, {'http': '208.65.174.66:80'}, {'http': '94.203.47.182:80'}, {'http': '197.189.235.82:80'}, {'http': '92.90.81.58:8081'}]
with open('zydh123','a')as f:
    for i in range(1,1000000):
        try:
            res = requests.get('http://zydh123.net/'+str(i)+'.html').content
            if not res:
                i=i-1
                continue
            if res=='<script>alert("tid error");window.location.href="/";</script>':
                print i
                continue
            tree=etree.HTML(res)
            div = tree.xpath('//*[@class="desc-box"]')[0]
            id=i
            title = div.xpath('*[@class="desc-title"]/h2/text()')[0]
            size = div.xpath('*[@class="desc-title"]/h2/em/text()')[0]
            magnet = div.xpath('*[@class="desc-list-item"][1]/div/a/@href')[0]
            emule = div.xpath('*[@class="desc-list-item"][2]/div/a/@href')[0]
            xiaomi = 'https://d.miwifi.com/d2r/?url='+base64.b64encode(str(magnet.encode('utf8')))+'&src=yyets&name='+urllib2.quote(title.encode('utf8'));
            print '\t'.join([str(i),title])
            f.write('\t'.join([str(i),title.encode('utf8'),size,magnet.encode('utf8'),emule,xiaomi])+'\n')
        except Exception,e:
            print e
            i=i-1
            continue
