#!/usr/bin/env python3
# coding: utf-8

import os
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

try:
    # 配置目录
    from conf.selenium_config import RES_PATH
except Exception:
    RES_PATH = 'D:/IDE/Test'  # 本机driver目录，末尾不加 “/”

if not os.path.exists(RES_PATH):
    print(RES_PATH, ' is not find')
    sys.exit()


def chromeDriver():
    driverPath = RES_PATH + "/chromedriver-2.45.exe"
    chromePath = RES_PATH + "/Chrome/chrome.exe"
    options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=" + chromeoptionPath))
    options.add_argument("--start-maximized")
    options.add_argument("--test-type")
    options.add_argument("allow-running-insecure-content")
    if os.path.isfile(chromePath):
        options.binary_location = chromePath
    dr = webdriver.Chrome(
        chrome_options=options, executable_path=driverPath, port=9976)
    dr.implicitly_wait(5)
    print('chrome start ...')
    return dr


def firefoxDriver():
    driverPath = RES_PATH + "/geckodriver-0.26.exe"
    firefoxPath = RES_PATH + "/Mozilla Firefox/firefox.exe"
    # profile = webdriver.FirefoxProfile(xx)
    # firefox_profile=profile
    if os.path.isfile(firefoxPath):
        binary = FirefoxBinary(firefoxPath)
        dr = webdriver.Firefox(
            executable_path=driverPath, firefox_binary=binary)
    else:
        dr = webdriver.Firefox(executable_path=driverPath)
    dr.maximize_window()
    dr.implicitly_wait(5)
    print('firefox start ...')
    return dr


def ieDriver():
    # DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
    # DesiredCapabilities.INTERNETEXPLORER['ignoreZoomSetting'] = True
    capabilities = DesiredCapabilities.INTERNETEXPLORER
    capabilities['ignoreZoomSetting'] = True
    capabilities['ignoreProtectedModeSettings'] = True
    driverPath = RES_PATH + "/IEDriverServer-2.53.1.exe"
    dr = webdriver.Ie(
        desired_capabilities=capabilities, executable_path=driverPath)
    dr.maximize_window()
    dr.implicitly_wait(5)
    print('ie start ...')
    return dr


if __name__ == '__main__':
    # chromeDriver()
    # firefoxDriver()
    ieDriver()
