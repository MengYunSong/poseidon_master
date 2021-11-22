#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-06-04
"""

from tests.data.elements.login_element import passLogin
from poseidon.ui.pc.base_page import BasePage

import logging
from poseidon.ui.util.location import *
from poseidon.base.RedisHelper import Redis_v2

# class MobileElement(BaseTextElement):
#     def __init__(self):
#         self.locator = passLogin.mobile_input
#
#
# class CaptchaCodeElement(BaseTextElement):
#     def __init__(self):
#         self.locator = passLogin.captcha_code_input
#
#






class LoginPage(BasePage):
    def open(self):
        BasePage.open(self,passLogin.url)


    def set_mobile_text(self, mobile):
        self.set_text(passLogin.mobile_input, mobile)

    def submit(self):
        # 输入手机号后出现图片验证码
        try:

            if self.is_displayed(passLogin.captcha_image):
                element = self.get_web_element(passLogin.captcha_image)
                key = self._get_redis_key(element=element)
                code = self._get_captcha(key)

                self.set_text(passLogin.captcha_code_input, code)

        except Exception as e:
            print(e)

        # 点击获取动态验证码按钮
        ele_bu = findClassName(driver=self.driver, name="hp-button-primary")
        ele_bu.click()

        # js = "element = arguments[0]; original_style = element.getAttribute('style'); element.setAttribute('style', original_style + \";border: 2px solid red;\");setTimeout(function(){element.setAttribute('style', original_style);}, 1000);"
        # self.driver.execute_script(js, ele_bu)

        import time
        time.sleep(5)







    def _get_redis_key(self, element):
        redis_token = element.get_attribute("src").split("=")
        key = redis_token[1][:-2]
        redis_key = "captcha:captcha_{}".format(key)
        logging.debug("redis-key is {}".format(redis_key))
        return redis_key


    def _get_captcha(self, key):
        r_client = Redis_v2(host="192.168.36.212", port="1012", db= "0")
        resp = r_client.getRedisValue(key=key, valueType="hash")
        resp = r_client.bytes_to_str(resp)
        code = resp['code']
        logging.debug("图片验证码结果 {}".format(code))
        return code


    def clean_redis_for_captcha(self,  name=None, ip=None):
        r_client_db1= Redis_v2(host="192.168.36.212", port="1012", db="1")
        r_client_db0= Redis_v2(host="192.168.36.212", port="1012", db="0")
        if name is not None:
            r_client_db1.delRedisValue("passport:js:loginfailed:username:{}".format(name))
            r_client_db0.delRedisValue("hjapp:soa:mobile:+86-{}:Login".format(name))

        if ip is not None:
            r_client_db1.delRedisValue("passport:js:loginfailed:ip:{}".format(ip))
            r_client_db1.delRedisValue("passport:imgCode:ip:validate:{}:count ".format(ip))










