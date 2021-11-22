# coding=utf-8

"""
@author:songmengyun
@file: test_example.py
@time: 2019/12/24

"""

import pytest
from datetime import datetime, timedelta
from tests.business.bus_api import bus_base as biz
from tests.data.data_api import data_base as base
from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env
from poseidon.base.Frequency import Frequency


class TestAPIDemo:

    testdata = [
        (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
        (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
    ]

    @classmethod
    def setup_class(cls):
        """ 所有case初始化操作 """
        cls.music_name = 'Jack'
        cls.url = biz.get_url(f"?name={cls.music_name}", base.url)
        cls.headers = {'Content-Type':'application/json'}

    @classmethod
    def teardown_class(cls):
        """ 所有case执行完后操作 """

    def setup_method(self):
        """ 每个case初始化操作 """

    def teardown_method(self, method):
        """ 每个case执行完后操作"""


    @pytest.mark.run([Env.qa, Env.yz, Env.prod], [Frequency.five_min])
    def test_api_get_music_info(self):
        '''验证获取歌曲API成功'''
        send_data = {"method":'get', "url":self.url, "headers":self.headers}
        check_point = {"code":200, "message":"成功!"}
        biz.send_music_and_respnse(send_data, check_point)

        # payload = {'username':"songmengyun@hujiang.com", 'password':"14a85607c6564c7d18de2e4474fb597a",'orgCode':'10002'}
        # send_data = {"method":'post', 'url':"https://yzpass-api.techedux.tech/login/loginByPassword", 'payload':payload, 'headers':self.headers}
        # check_point = {"status": 0,}
        # biz.send_music_and_respnse(send_data, check_point)


