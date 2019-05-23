# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/4/4  14:03 
# 文件名称   ：webtest.PY
# 开发工具   ：PyCharm

from selenium import webdriver
import unittest
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.0.192:8888/login.html")
        time.sleep(2)

    def test_login(self):
        self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号']").send_keys("18351921721")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("cxli123")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("dfewfe")
        self.driver.find_element_by_xpath("//button[@class='login-btn']").click()
        time.sleep(2)
        #校验网站标题
        title = self.driver.find_element_by_xpath("//span[@class='ems-title']").text
        #print(title)
        assert title == "车300伽马风控系统"

        self.driver.find_element_by_xpath("//span[@title='贷后资产监控']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[contains(text(),'贷后监控列表')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='资产编号']").send_keys("1000262874")
        time.sleep(1)
        self.driver.find_element_by_xpath("//form[contains(@class,'ant-form ant-form-horizontal ant-advanced-search-form')]//button[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("// span[contains(text(), '查看')]").click()
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(1)
        #校验资产编号
        #//span[@class ='reportId']
        reportID = self.driver.find_element_by_xpath("//span[@class ='reportId']").text
        if reportID.endswith('1000262874') == True:
            print("报告编号与资产编号对应")
        else:
            print("报告编号与资产编号不对应")
        time.sleep(5)

        #切换回来
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath("//form[@class='ant-form ant-form-horizontal ant-advanced-search-form']//button[2]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='资产编号']").send_keys("11000262874")
        time.sleep(1)
        self.driver.find_element_by_xpath("//form[@class='ant-form ant-form-horizontal ant-advanced-search-form']//button[1]").click()
        time.sleep(1)
        print(self.driver.find_element_by_xpath("//span[contains(text(),'暂无数据')]").text)

        # self.driver.find_element_by_xpath("//span[contains(text(),'系统设置')]").click()
        # self.driver.find_element_by_xpath("//a[contains(text(),'用户管理')]").click()
        # self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
        # self.driver.find_element_by_xpath("//div[contains(text(),'请选择归属机构')]").click()
        # self.driver.find_element_by_xpath("//li[contains(text(),'0s7a2rcd')]").click()


        # self.driver.find_element_by_xpath("//span[@title='贷前反欺诈']").click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath("//a[contains(text(),'贷前反欺诈')]").click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath("// span[2] // button[1]").click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath("//div[contains(@class,'ant-col-18 ant-form-item-control-wrapper')]//div[contains(@class,'ant-select-selection__placeholder')][contains(text(),'全部')]").click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath("//li[contains(text(),'重庆车云')]").click()
        # print("******"+str(self.driver.find_element_by_xpath("//li[contains(text(),'重庆车云')]")))
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()