#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-06-04
"""

from selenium.webdriver.common.by import By
from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env

class PassLogin:
    @property
    def url(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: "http://qapass.hujiang.com",
            Env.yz: "http://yzpass.hujiang.com",
            Env.prod: "http://pass.hujiang.com"
        })

    @property
    def mobile_input(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.XPATH, '//*[@id="hp-pass-box"]/div[1]/div[1]/div[2]/div[2]/div/input')
        })

    @property
    def captcha_code_input(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.XPATH, '//*[@id="hp-pass-box"]/div[1]/div[1]/div[2]/div[3]/div[1]/div/div[2]/input'),
        })

    @property
    def captcha_image(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.CLASS_NAME, 'hp-captcha-image'),
        })

    @property
    def login_button(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: (By.CLASS_NAME, 'hp-button-primary hp-button-hj  hp-button-pc hp-button-disabled hp-mobile-v-btn'),
        })
passLogin = PassLogin()
