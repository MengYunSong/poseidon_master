# # coding=utf-8
#
# """
# @author:songmengyun
# @file: bus_ui.py
# @time: 2019/12/25
#
# """
#
#
# # from data.data_web import data_web
# from .data_web import data_web
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# import logging
# from poseidon.ui.pc.base_page import BasePage
# from poseidon.base import CommonBase as cb
#
#
#
# def page(page_name, driver):
#     # 统一管理所有页面
#     _pages = {
#         'baidu': PageBaiduSearch(driver),
#     }
#
#     return _pages.get(page_name)
#
#
#
# class PageBaiduSearch(BasePage):
#
#     def open_baidu_url(self, describe=None):
#         '''打开百度首页首页'''
#         if cb.describe: logging.info(describe)
#         self.open(baidu.url[0])
#         element = WebDriverWait(self.driver, 5, 0.5).until(EC.title_is(baidu.url[1]))
#         cb.checkEqual(element, True)
#
#     def input_text_and_search(self, describe=None):
#         '''搜索"poseidon并验证结果"'''
#         if describe: logging.info(describe)
#         try:
#             self.click_element(baidu.search_box, is_button=False)
#             self.set_text(baidu.search_box, 'poseidon')
#             self.click_element(baidu.search_button[0], is_button=True)
#             element = WebDriverWait(self.driver, 5, 0.5).until(EC.title_is(baidu.search_button[1]))
#             cb.checkEqual(element, True)
#         except Exception as e:
#             logging.info(e)
#             raise e
