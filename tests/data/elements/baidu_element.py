#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-06-10
"""

from selenium.webdriver.common.by import By
from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env


class Baidu:

    @property
    def url(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: ['https://www.baidu.com','百度一下，你就知道']
        })

    @property
    def news_link_linktext(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.LINK_TEXT, '新闻'),
        })

    @property
    def search_input(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.ID, 'kw'),
        })

    @property
    def search_button(self):
        return cb.get_value_from_env_data_dict({
            # Env.qa: (By.ID, 'su'),
            Env.qa: [(By.XPATH, '//*[@id="su"]'),'poseidon_百度搜索']
        })

    @property
    def search_box(self):  # 百度首页
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.XPATH, '//*[@id="kw"]')
        })


baidu = Baidu()
