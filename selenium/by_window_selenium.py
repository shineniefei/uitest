#!/usr/bin/env python3
# coding:utf-8

from common_driver import chromeDriver


def login(url):

    dr = chromeDriver()
    dr.get(url)
    window_0 = dr.current_window_handle  # 获得打开的第一个窗口句柄
    dr.find_element_by_id('button').click()
    windows_all = dr.window_handles  # 获取所有窗口句柄
    for window in windows_all:  # 在所有窗口中查找弹出窗口
        if window != window_0:
            dr.switch_to_window(window)
            dr.close()
    dr.switch_to_window(window_0)
    return dr


if __name__ == '__main__':
    pass
