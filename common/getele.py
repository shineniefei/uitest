#!/usr/bin/env python3
# coding:utf-8
'''
by_id= "id"
by_xpath = "xpath"
by_link_text = ""
by_partial_text = "partial link text"
by_name = "name"
by_tag_name = "tag name"
by_class_name = "class name"
by_css_selector = "css selector"
'''

# driver.find_element(getby(key)).send_keys("yoyoketang")


def setele(key, by, value):
    bys = {
        'id', 'xpath', 'link text', 'partial link text', 'name', 'tag name',
        'class name', 'css selector'
    }
    if by in bys:
        a = key
        b = (by, value)
    else:
        return 'key is not avilable'
    return a, b


def getele(key):
    types = key
    value = key
    return types, value


if __name__ == "__main__":
    a = getele('111')
    print(a)
