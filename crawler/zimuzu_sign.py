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
import datetime
def sign(account,password):
    try:
        print 'signing...'
        client_id=str(uuid.uuid1())
        headers={'Accept':' application/json, text/javascript, */*; q=0.01',
        'X-DevTools-Emulate-Network-Conditions-Client-Id':client_id,
        'X-Requested-With':'XMLHttpRequest',
        'X-FirePHP-Version':'0.0.6',
        'Host':'www.zimuzu.tv',
        'Origin':'http://www.zimuzu.tv',
        'Referer':'http://www.zimuzu.tv/user/login',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
        'Referer':' http://www.zimuzu.tv/user/sign',
        'Accept-Encoding':' gzip, deflate, sdch',
        'Accept-Language':' zh-CN,zh;q=0.8'
        }
        resHeaders = requests.get('http://www.zimuzu.tv/user/login',headers=headers).headers
        session = resHeaders['set-cookie'][10:36]
        headers['Cookie']='PHPSESSID='+session+'; CNZZDATA1254180690=111511151-1430530153-%7C1430530153'
        data={'account':account,
        'password':password,
        'remember':'1',
        'url_back':'http://www.zimuzu.tv/user/sign'}
        res = requests.post('http://www.zimuzu.tv/User/Login/ajaxLogin',data=data,headers=headers)
        cookie = res.headers['set-cookie']
        cookie=cookie.replace('GINFO=deleted;','').replace('GKEY=deleted;','')
        GINFO=re.search('GINFO=uid[^;]+',cookie).group(0)+";"
        GKEY=re.search('GKEY=[^;]+',cookie).group(0)+";"
        CPS = 'yhd%2F'+str(int(time.time()))+";"
        Cookie =' PHPSESSID='+session+'; '+CPS+(GINFO+GKEY)*3
        headers['Cookie']=Cookie
        requests.get("http://www.zimuzu.tv/user/sign",headers=headers).content
        print 'wait for 20 seconds...'
        time.sleep(20)
        content = requests.get("http://www.zimuzu.tv/user/sign/dosign",headers=headers).json()
        print "sign success! " if content['data']!=False else ("signed! " if content['data']==False else "sign failed! "+content),content['status']
        print str(datetime.datetime.now())
    except Exception,e:
        raise Exception('err',str(e))
while True:
    try:
        sign('用户名','密码')
        break
    except Exception,e:
        print e
        time.sleep(300)

