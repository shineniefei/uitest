#!/usr/bin/env python3
# coding:utf-8
'''
上一步：个贷匹配通道
功能：注册借款端，借款端开户，借款端鉴权，借款端签约
说明：恒慧融
下一步：服务部待审核
'''

import time

import pymysql
from selenium.webdriver.support.select import Select

from common_driver import chromeDriver


# 查询
def query(sql, db_config):
    print('execute sql : ', sql)
    try:
        conn = pymysql.connect(**db_config)  # 创建连接
        with conn.cursor() as cursor:  # 创建游标 关闭游标
            cursor.execute(sql)  # 执行SQL，并返回收影响行数
            rs = cursor.fetchone()  # 返回一元数组
            # rs = cursor.fetchall()  # 返回二元数组
            conn.commit()  # 提交保存
        print()
        print('effect_row = ', format(cursor.rowcount), 'result : ', str(rs))
    finally:
        conn.close()  # 关闭连接
    return rs


# 恒慧融借款端注册
def register_by_db(phone, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG):
    is_register_sql = 'select userid from `users` where phone = \"%s\" ;' % phone
    tem = query(is_register_sql, HHRLOAN_DB_CONFIG)
    if tem is None:
        query_sql = 'select b.client_name,b.id_num from crm_intopieces_dk b where b.client_phone = \"%s\" ;' % phone
        tup = query(query_sql, CRM6_DB_CONFIG)
        name = tup[0]
        idcard = tup[1]
        insert_sql = 'insert into `test_hhrloan`.`users` (`username`,`password`,`phone`,`real_name`,`identity_no`)\
             VALUES ( \"%s\" , "e6032a45118887b87d9206bc013e22ed",\"%s\",\"%s\",\"%s\")' % (
            phone, phone, name, idcard)
        query(insert_sql, HHRLOAN_DB_CONFIG)
        print(str(phone) + ' register success')
    else:
        print(str(phone) + ' already register')


# # 恒慧融借款端注册(因有图片验证码，无法获取手机验证码)
# def resigner(phone):
# querysql = 'select a.account_number ,b.client_name,b.id_num from crm_account_mes_dk a,crm_intopieces_dk b\
#     where a.intopieces_id= b.id and b.client_phone = \"%s\" ;' % phone
#     tup = query(querysql, CRM6_GTDJ_DB_CONFIG)
#     account_number = tup[0]
#     name = tup[1]
#     idcard = tup[2]
#     dr = chromeDriver()
#     dr.get(HHRHOST + '/register')
#     print(dr.title)
#     dr.find_element_by_id('phone').send_keys(phone)
#     dr.find_element_by_id('pass_word').send_keys('crm123')
#     dr.find_element_by_id('re_pass').send_keys('crm123')
#     dr.find_element_by_id('img_error').send_keys('0000')
#     dr.find_element_by_id('key_code').click()
#     dr.find_element_by_id('telcode_error').send_keys('111111')
#     dr.find_element_by_id('btn_Submit').click()
#     dr.find_element_by_id('l_user').send_keys(name)
#     dr.find_element_by_id('J_typeNum').send_keys(idcard)
#     dr.find_element_by_id('s_agreement').click()
#     dr.find_element_by_id('btn_Submit1').click()
#     print('resigner success')


# 登录
def hhr_login(HHRHOST, phone, pwd):
    dr = chromeDriver()
    dr.get(HHRHOST + '/login')
    dr.find_element_by_id('l_user').send_keys(phone)
    dr.find_element_by_id('l_pwd').send_keys(pwd)
    dr.find_element_by_id('img_error').send_keys('0000')
    dr.find_element_by_id('login_but').click()
    time.sleep(1)
    print(str(phone) + ' hhr_login success')
    return dr


# 开户
def openacc(dr, HHRHOST, bank, bankno, phone):
    if (dr.find_element_by_xpath("//a[@onclick='openacc()']")):
        dr.get(HHRHOST + '/openacc')
        time.sleep(2)
        # query_sql = 'SELECT banknum from crm_intopieces_info_dk a LEFT JOIN crm_intopieces_dk b\
        #      on b.id = a.ip_id where b.client_phone = \"%s\" ;' % phone
        # tup = query(query_sql, CRM6_DB_CONFIG)
        # if tup:
        #     bankno = tup[0]
        Select(
            dr.find_element_by_xpath(
                "//select[@id='bindBank' and @class='zcNoEmpty']")
        ).select_by_visible_text(bank)
        dr.find_element_by_id('bindMobile').send_keys(phone)
        dr.find_element_by_id('check1').click()
        dr.find_element_by_id('zcSubmit').click()
        time.sleep(1)
        # dr.find_element_by_class_name('layui-layer-btn0').click()
        time.sleep(2)
        dr.find_element_by_id('bankcardNo').send_keys(bankno)
        time.sleep(1)
        dr.find_element_by_id('sendSmsVerify').click()
        # window_1 = dr.current_window_handle  # 获得打开的第一个窗口句柄
        # window_current = dr.current_window_handle  # 在这里得到当前窗口句柄
        # windows_all = dr.window_handles  # 获取所有窗口句柄
        # for window in windows_all:  # 在所有窗口中查找弹出窗口
        #     if window != window_current:
        #         dr.switch_to_window(window_current)
        # dr.switch_to_window(window_1)  # 返回到主窗口页面
        time.sleep(1)
        dr.find_element_by_xpath(
            "//div[@id='alertLayer-2']//div[2]//a").click()
        dr.find_element_by_id('smsCode').send_keys('111111')
        dr.find_element_by_id('password').send_keys('crm123')
        dr.find_element_by_id('confirmPassword').send_keys('crm123')
        dr.find_element_by_id('nextButton').click()
        time.sleep(60)
        print('openacc success')


# 鉴权
def ackAuth(dr, HHRHOST):
    dr.get(HHRHOST + '/ackAuth')
    time.sleep(1)
    # print('宝付鉴权')
    # dr.find_element_by_xpath("//form[@id='ackform']/li[1]/input[2]").click()
    # time.sleep(3)
    # dr.find_element_by_xpath("//form[@id='ackform']/li[1]/input[3]").send_keys(
    #     '12')
    # dr.find_element_by_xpath("//form[@id='ackform']/li[1]/input[5]").click()
    # time.sleep(5)
    # print('通联鉴权')
    dr.find_element_by_xpath("//form[@id='ackform']/li[2]/input[2]").click()
    time.sleep(3)
    dr.find_element_by_xpath("//form[@id='ackform']/li[2]/input[3]").send_keys(
        '12')
    dr.find_element_by_xpath("//form[@id='ackform']/li[2]/input[5]").click()
    time.sleep(5)
    # print('快付通鉴权')
    # dr.find_element_by_xpath("//form[@id='ackform']/li[3]/input[2]").click()
    # time.sleep(15)
    # dr.find_element_by_xpath("//form[@id='ackform']/li[3]/input[3]").send_keys(
    #     '111111')
    # dr.find_element_by_xpath("//form[@id='ackform']/li[3]/input[5]").click()
    # time.sleep(5)
    # print('连连鉴权')
    dr.find_element_by_xpath("//form[@id='ackform']/li[4]/input[2]").click()
    time.sleep(3)
    dr.find_element_by_xpath("//form[@id='ackform']/li[4]/input[3]").send_keys(
        '12')
    dr.find_element_by_xpath("//form[@id='ackform']/li[4]/input[5]").click()
    time.sleep(5)
    print('ackAuth success')


# 签约
def center(dr, HHRHOST):
    dr.get(HHRHOST + '/center')
    dr.find_element_by_class_name('s_org').click()
    time.sleep(1)
    dr.find_element_by_class_name('layui-layer-btn0').click()
    time.sleep(1)
    dr.find_element_by_class_name('layui-layer-btn0').click()
    dr.find_element_by_id('s_agreement').click()
    dr.find_element_by_id('accreditBtn').click()
    time.sleep(5)
    print('center success')


# 换卡@TODO
def changeCard(dr, HHRHOST, phone, bank, bankno):
    dr.get(HHRHOST + '/center')
    time.sleep(1)
    dr.find_element_by_id("changeBtn").click()
    Select(
        dr.find_element_by_xpath(
            "//select[@id='bindBank' and @class='zcNoEmpty']")
    ).select_by_visible_text(bank)
    dr.find_element_by_id('bindBankNo').send_keys(bankno)
    Select(dr.find_element_by_xpath(
        "//select[@id='province']")).select_by_visible_text('北京市')
    dr.find_element_by_id('bindMobile').send_keys(phone)
    time.sleep(2)
    dr.find_element_by_id('zcSubmit').click()
    time.sleep(2)
    dr.find_element_by_class_name('layui-layer-btn0').click()
    time.sleep(3)
    print('changeCard success')


def main(url, phone, pwd, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG):
    register_by_db(phone, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG)
    dr = hhr_login(url, phone, pwd)
    openacc(dr, url, bank, bankno, phone)
    ackAuth(dr, url)
    center(dr, url)
    # changeCard(dr, phone, bank, bankno)
    dr.close()
    # dr.quit()


def loop(url, phone, endphone, pwd, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG):
    while phone <= endphone:
        try:
            main(url, phone, pwd, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG)
            phone += 1
        except Exception as e:
            print(str(phone) + ' is error!')
            phone += 1
            # dr.quit()


if __name__ == '__main__':
    pwd = 'crm123'
    url = 'http://10.100.19.183'
    bank = '建设银行'
    bankno = '6210810730008929243'
    # 测试gtdj库
    CRM6_DB_CONFIG = {
        'host': '10.100.13.238',
        'port': 3306,
        'user': 'crmdk_admin',
        'password': 'crmdkadmin123!@#',
        'db': 'credithc_crmdk_cs',
        'charset': 'utf8mb4',
    }
    # 测试借款端数据库
    HHRLOAN_DB_CONFIG = {
        'host': '10.150.20.45',
        'port': 3306,
        'user': 'test_hhrloan',
        'password': 'meili76s',
        'db': 'test_hhrloan',
        'charset': 'utf8mb4',
    }
    # url = 'http://10.160.13.116/'
    # CRM6_DB_CONFIG = {
    #     'host': '10.100.13.238',
    #     'port': 3306,
    #     'user': 'crmdk_admin',
    #     'password': 'crmdkadmin123!@#',
    #     'db': 'credithc_crmdk_cs_copy_116',
    #     'charset': 'utf8mb4',
    # }
    # HHRLOAN_DB_CONFIG = {
    #     'host': '10.160.13.124',
    #     'port': 3306,
    #     'user': 'test_hhrloan',
    #     # 'password': 'meili76s',
    #     'password': 'l5fmMkOQRRrn7Mnw',
    #     'db': 'test_hhrloan',
    #     'charset': 'utf8mb4',
    # }
    phone = 14709031816
    endphone = 14709031817
    main(url, phone, pwd, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG)
    # loop(url, phone, endphone, pwd, CRM6_DB_CONFIG, HHRLOAN_DB_CONFIG)
