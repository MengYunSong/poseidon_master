# coding=utf-8

"""
@author:songmengyun
@file: test_baidu_search.py
@time: 2019/12/17

"""

import pytest
import time
import logging
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency
from selenium import webdriver
from tests.business.pages_ui.page_factory import page

'''
前提条件：
查看chrome版本：chrome://version
1. 下载对应chromedriver: https://npm.taobao.org/mirrors/chromedriver/
2. mac电脑把chromedriver放在/usr/local/bin，会默认读取
3. 安装selenium, 默认poseidon安装包含

'''


class TestBaidu():

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_baidu_search(self, drivers):
        '''验证百度搜索：通过selenium插件实现'''

        baidu = page("baidu", drivers)
        baidu.open_baidu_url('【step1】打开百度页面')
        baidu.input_text_and_search('【step2】输入poseidon并验证搜索结果')

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_baidu_search1(self, selenium):
        '''验证百度搜索: 通过pytest-selenium插件实现'''

        baidu = page("baidu", selenium)
        baidu.open_baidu_url('【step1】打开百度页面')
        baidu.input_text_and_search('【step2】输入poseidon并验证搜索结果')

    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_headless(self, driver_headless):
        '''无头模式'''
        # options = webdriver.ChromeOptions()   # option对象
        # options.add_argument('headless')    # 给option添加属性
        # driver = webdriver.Chrome(options=options)
        # driver.get('http://www.baidu.com')
        # time.sleep(3)
        # driver.close()

        baidu = page("baidu", driver_headless)
        baidu.open_baidu_url('【step1】打开百度页面')
        baidu.input_text_and_search('【step2】输入poseidon并验证搜索结果')
