#!/usr/bin/env python3
# coding: utf-8

import os

from appium import webdriver


def appium_dirver(desired_caps):
    print(os.system('adb devices'))
    # os.system('appium')
    if desired_caps is None:
        desired_caps = {
            'platformName': 'Android',  # 平台名称
            'platformVersion': '5.1.1',  # 系统版本号
            'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
            'appPackage': 'com.zhuanzhuan.hunter',  # apk的包名
            'appActivity':
            'com.zhuanzhuan.hunter.bussiness.main.MainActivity',  # activity 名称(adb logcat | grep Displayed )
        }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                          desired_caps)  # 连接Appium
    print("appium start ...")
    return dr


if __name__ == "__main__":
    appium_dirver(None)
