# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/4/4  11:24 
# 文件名称   ：test02.PY
# 开发工具   ：PyCharm

from selenium import webdriver
import unittest
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.0.192:8888/login.html")
        time.sleep(2)

    def test_login(self):
        self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号']").send_keys("18351921721")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("cxli123")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("dfewfe")
        self.driver.find_element_by_xpath("//button[@class='login-btn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@title='贷前反欺诈']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[contains(text(),'贷前反欺诈')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("// span[2] // button[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[contains(@class,'ant-col-18 ant-form-item-control-wrapper')]//div[contains(@class,'ant-select-selection__placeholder')][contains(text(),'全部')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[contains(text(),'重庆车云')]").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()