#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-06-04
"""

import pytest
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency
import poseidon.base.CommonBase as cb
# from business.pages.page_factory import page
from tests.business.pages_ui.page_factory import page




class Test_pass_login:
    @pytest.mark.run([Env.qa], [Frequency.one_min])
    def test_two(self, driver):
        """
        用户中心pass登录
        """
        kanon = page("login_pc", driver)
        kanon.open()

        kanon.clean_redis_for_captcha(name="18019762900", ip="172.16.20.38")
        kanon.set_mobile_text("18019762900")
        kanon.submit()

    @pytest.mark.run([Env.qa], [Frequency.one_min])
    def test_three(self, driver):
        """
        百度首页 测试
        """
        kanon = page("baidu", driver)
        kanon.open()
        kanon.search("smy")

    @pytest.mark.run([Env.qa], [Frequency.one_min])
    def test_four(self, driver):
        """
        百度首页修改新闻链接为 http://www.taobao.com
        """
        kanon = page("baidu", driver)
        kanon.open()
        kanon.change_news_link()

    @pytest.mark.run([Env.qa], [Frequency.one_min])
    def test_five(self, selenium):
        cb.tc_describe("百度首页修改新闻链接为 http://www.taobao.com")
        kanon = page("baidu", selenium)
        kanon.open()
        kanon.change_news_link()

    @pytest.mark.run([Env.qa], [Frequency.one_min])
    def test_six(self, driver_headless):
        cb.tc_describe("百度首页修改新闻链接为 http://www.taobao.com")
        kanon = page("baidu", driver_headless)
        kanon.open()
        kanon.change_news_link()







