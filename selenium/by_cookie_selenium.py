#!/usr/bin/env python3
# coding:utf-8

import requests

from common_driver import chromeDriver


def postGetCookie():
    # Headers信息
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # 实际登录地址
    url = 'http://localhost/loging'
    # 实际form信息
    data = '''staff_login_name=13888888888&staff_pwd=*****&verify=0000'''
    # 发起请求
    r = requests.post(url=url, data=data, headers=headers)
    # 取出cookie
    cookie = {}
    for cookies in r.cookies:
        cookie = cookies.name + '=' + cookies.value
        # cookie['name'], cookie['value'] = cookies.name, cookies.value
    print(cookie)
    return cookie


def seleniumByCookie(url, cookie):
    # 启动浏览器
    dr = chromeDriver()
    # 登录尝试
    dr.get(url)
    # 增加 cookie = {'name': 'PHPSESSID', 'value': r.cookies.value}
    dr.add_cookie(cookie)
    dr.get(url)


if __name__ == '__main__':
    pass
