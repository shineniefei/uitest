#!/usr/bin/env python3
# coding:utf-8

import datetime

from selenium.webdriver.support.select import Select


def customer(dr, url):
    dr.get(url)
    dr.switch_to_alert().accept()

    Select(dr.find_element_by_id('loan_qs')).select_by_visible_text('12个月')
    dr.find_element_by_xpath("//input[@class='input jkMoney']").send_keys(
        50000)
    Select(dr.find_element_by_id('loan_usage')).select_by_visible_text('教育支出')
    dr.find_element_by_xpath("//form[@id='J_loan_form']/p/a").click()
    dr.switch_to_alert().accept()

    toda_yym = datetime.datetime.now().strftime('%Y-%m')

    # 用js方法输入日期
    # js_value = f'''document.getElementsByClassName("input year").value="{toda_yym}"'''
    # dr.execute_script(js_value)

    # 去掉元素的readonly属性，输入时间
    # js = '''document.getElementsByClassName("input year").removeAttribute("readonly")'''  # 1.原生js，移除属性
    js = '''$("input[class='input year']").removeAttr('readonly')'''  # 2.jQuery，移除属性
    # js = "$('input[class=input year]').attr('readonly',false)"  # 3.jQuery，设置为false
    # js = "$('input[class='input year']').attr('readonly','')"  # 4.jQuery，设置为空（同3）
    dr.execute_script(js)
    dr.find_element_by_xpath("//input[@class='input year']").send_keys(
        toda_yym)

    toda_yymd = datetime.datetime.now().strftime('%Y-%m-%d')
    js1 = '''$("input[class='input time']").removeAttr('readonly')'''
    dr.execute_script(js1)
    dr.find_element_by_xpath("//input[@class='input time']").send_keys(
        toda_yymd)


if __name__ == '__main__':
    pass
