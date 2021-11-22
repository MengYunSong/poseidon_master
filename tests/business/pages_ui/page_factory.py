#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       songmengyun
   date:         2019-06-04
"""


from tests.business.pages_ui.login_page import LoginPage
from tests.business.pages_ui.baidu_page import BaiduPage


def page(page_name, driver):
    # 统一管理所有页面
    _pages = {
        'login': LoginPage(driver),
        'baidu': BaiduPage(driver)
    }

    return _pages.get(page_name)
