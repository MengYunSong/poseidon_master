#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-06-10
"""

from poseidon.ui.pc.base_page import BasePage
from poseidon.base import CommonBase as cb
from tests.data.elements.baidu_element import baidu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BaiduPage(BasePage):

    def news_link(self):
        # aa = self.is_displayed(baidu.news_link_linktext)
        # print(aa)
        pass

    def search(self, keyword):
        self.set_text(baidu.search_input, keyword)
        self.click_element(baidu.search_button)

    def change_news_link(self):
        element = self.get_web_element(baidu.news_link_linktext)
        print("修改前 {}".format(element.get_attribute("href")))

        js = 'arguments[0].href="http://www.taobao.com"'
        self.driver.execute_script(js, element)
        self.wait(3)
        element_1 = self.get_web_element(baidu.news_link_linktext)
        print("修改后 {}".format(element_1.get_attribute("href")))
        self.click_element(baidu.news_link_linktext)

    def open_baidu_url(self, describe=None):
        '''打开百度首页首页'''
        if describe: logging.info(describe)
        self.open(baidu.url[0])
        element = WebDriverWait(self.driver, 5, 0.5).until(EC.title_is(baidu.url[1]))
        cb.checkEqual(element, True)

    def input_text_and_search(self, describe=None):
        '''搜索"poseidon并验证结果"'''
        if describe: logging.info(describe)
        try:
            self.click_element(baidu.search_box, is_button=False)
            self.set_text(baidu.search_box, 'poseidon')
            self.click_element(baidu.search_button[0], is_button=True)
            element = WebDriverWait(self.driver, 5, 0.5).until(EC.title_is(baidu.search_button[1]))
            cb.checkEqual(element, True)
        except Exception as e:
            logging.info(e)
            raise e






