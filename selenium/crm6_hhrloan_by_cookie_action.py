#!/usr/bin/env python3
# coding:utf-8

from urllib import parse
from urllib import request
import json
import requests

data = {}
data['username'] = 12314
data['password'] = 'crm123'
data['img_code'] = '0000'


# 后台登录
def cookielogin(data):
    # Headers信息
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = 'http://10.100.19.183/loginAjax'
    params = ''
    for key in data:
        params = params + key + "=" + data[key] + "&"
    data = params
    # 发起请求
    r = requests.post(url=url, data=data, headers=headers)
    # 取出cookie
    cookie = {}
    for cookies in r.cookies:
        cookie = cookies.name + '=' + cookies.value
    print(cookie)
    return cookie


# 后台预鉴权
def preAckAuth(Cookie, third_code):
    url = 'http://10.100.19.183/AckAuth'
    # Headers信息
    headers = {"Connection": "keep-alive"}
    headers['Cookie'] = Cookie
    data = {}
    data['type'] = 'sendsms'
    data['third_code'] = third_code
    # 发起请求
    r = requests.post(url=url, data=data, headers=headers)
    print(r.text)
    back = json.loads(r.text)
    data = back['data']
    print(data)
    return data


# 后台鉴权
def AckAuth(Cookie, third_code, pre_bizid):
    url = 'http://10.100.19.183/AckAuth'
    headers = {"Connection": "keep-alive"}
    headers['Cookie'] = Cookie
    data = {}
    data['type'] = 'ackSubmit'
    data['sms_code'] = '111111'
    data['third_code'] = third_code
    data['pre_bizid'] = pre_bizid
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url=url, data=data, headers=headers)
    with request.urlopen(req) as f:
        back = f.read().decode('utf-8')
    print(back)


if __name__ == '__main__':
    pass
