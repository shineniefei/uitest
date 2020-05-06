#!/usr/bin/env python3
# coding: utf-8
import os
import sys

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from splinter import Browser
from xvfbwrapper import Xvfb

try:
    # 配置目录
    from conf.selenium_config import RES_PATH
except Exception:
    RES_PATH = 'D:/IDE/Test'  # 本机driver目录，末尾不加 “/”

if not os.path.exists(RES_PATH):
    print(RES_PATH, ' is not find')
    sys.exit()


# TODO
def splinter_xvfb():

    vdisplay = Xvfb(width=1280, height=720)
    vdisplay.start()
    print('Start...')
    browser = webdriver.Firefox()
    browser.get('http://52sox.com')
    title = browser.title
    print(title)
    print("Clean...")
    browser.close()
    vdisplay.stop()


def splinter_chrome():
    driverPath = RES_PATH + "/chromedriver-2.45.exe"
    chromePath = RES_PATH + "/Chrome/chrome.exe"
    # chrome_options = Options()
    options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=" + chromeoptionPath))
    options.add_argument("--start-maximized")
    options.add_argument("--test-type")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("allow-running-insecure-content")
    if os.path.isfile(chromePath):
        options.binary_location = chromePath
    br = Browser(
        driver_name='chrome', options=options, executable_path=driverPath)
    return br


def splinter_firefox():
    driverPath = RES_PATH + "/geckodriver-0.23.0.exe"
    firefoxPath = RES_PATH + "/Mozilla Firefox/firefox.exe"
    # profile = webdriver.FirefoxProfile(xx)
    # firefox_profile=profile
    if os.path.isfile(firefoxPath):
        binary = FirefoxBinary(firefoxPath)
    else:
        binary = None
    br = Browser(
        driver_name='firefox',
        executable_path=driverPath,
        firefox_binary=binary)
    return br


if __name__ == "__main__":
    browser = splinter_chrome()
    browser.visit('https://www.baidu.com')
    # browser1 = splinter_firefox()
    # browser1.visit('https://www.baidu.com')
