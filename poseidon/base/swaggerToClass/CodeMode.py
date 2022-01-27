# -*- coding:utf8 -*-

import getpass
from datetime import datetime

class ApiClassCodeMode(object):

    def generate_import(self, file_name='demo.py'):
        """接口类导入的模块"""
        code = """
# coding=utf-8

'''
@author:{0}
@file: {1}.py
@time: {2}

'''

from business.bus_com.utils import SendApiRequest
from business.bus_com.base_obj import BaseObj
                """.format(getpass.getuser(), file_name, datetime.now())

        return code

    def generate_api_class(self, class_name, base_name, api_desc, host, uri, method):
        code = """

class {api_class_name}({base_name}):
    def __init__(self, headers=None):
        super().__init__()
        self.info = \"{api_desc}\"
        self.host = \"http://{host}\"
        self.uri = \"{uri}\"
        self.method = \"{method}\"
        self.headers = headers
        self.body = self.Body()
        self.resp = self.Resp()
        self.status = 1
        
        """.format(api_class_name=class_name,
                   base_name=base_name,
                   api_desc=api_desc,
                   host=host,
                   uri=uri,
                   method=method
                   )
        return code

    def generate_send_check_method(self):
        code = """
        
    def send_request_then_check(self, http_status_exp=200, status_exp=0, db_check=False, mq_check=False):
        '''发送请求并校验发送结果'''

        url = self.host + self.uri
        send_resp_obj = SendApiRequest(self.method, url, self.body, self.resp, headers=self.headers)

        # 发送前操作: 比如清除mq数据
        
        # 发送请求
        resp_act = send_resp_obj.send_request(status_exp=status_exp, http_status_exp=http_status_exp)
        send_resp_obj.check_response(resp_act, self.resp, belong=True)

        # 验证MQ
        if mq_check == True:
            pass

        # 验证DB
        if db_check == True:
            pass     
        
        """
        return code



class TestCaseCodeMode(object):

    def generate_import(self, uri, method, desc, file_name='demo.py'):
        """case类导入的模版"""
        code = """
# coding=utf-8

'''
@author:{author}
@file: {file}.py
@time: {time_now}

'''

'''
url: {uri}
method：{method}
description: {desc}

'''

import pytest
import logging
from Tetis.base import CommonBase as cb
from Tetis.base.Env import Env
from Tetis.base.Frequency import Frequency
                    """.format(author=getpass.getuser(), file=file_name, time_now=datetime.now(),
                               uri=uri, method=method, desc=desc)

        return code

    def code_model_header(self, uri, api_class_name):
        code = """


class {api_class_name}():

    @classmethod
    def setup_class(cls):
        cls.uri = '{uri}'

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass
    """.format(api_class_name=api_class_name, uri=uri)
        return code



class DBCodeModel(object):
    def __init__(self):
        pass

    def import_code(self):
        import_str = """
from hujiang.business.apiPeewee.customerFields import MyBitField, MyDateTimeField
from hujiang.conf.ecm_config import get_database

        """
        return import_str

    def db_code(self, db_name):
        db_str = """
database = get_database('{db_name}')
        """.format(db_name=db_name)
        return db_str


api_obj_code_model = ApiClassCodeMode()
test_case_code_model = TestCaseCodeMode()
db_code_model = DBCodeModel()

