#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2018/4/24 15:50
"""

from  selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

dr = webdriver.Chrome()
dr.get("http://test.iyoujia.com/")
# dr.find_element_by_xpath("").click()
# dr.find_element_by_xpath("").send_keys("张佳恒")
dr.find_element_by_xpath("//*[@id='indexPage']/div[6]/div[2]/div[1]/div[7]/div[1]/div/div[1]/input").click()
sleep(2)
# s = dr.find_element_by_id("province_select")
# Select(s).select_by_value("30")

js = "var q=document.getElementById('province_select').scrollTop=9000"
dr.execute_script(js)
sleep(2)
dr.find_element_by_xpath("//*[@id='province_select']/li[30]").click()
