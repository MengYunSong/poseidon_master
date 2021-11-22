# coding=utf-8

"""
@author: songmengyun
@file: test_login.py
@time: 2021/11/17

"""

import pytest


def login(username, password):
    """模拟登录"""
    user = "linux超"
    pwd = "linux超哥"
    if user == username and pwd == password:
        return {"code": 1001, "msg": "登录成功", "data": 'success'}
    else:
        return {"code": 1000, "msg": "用户名或密码错误", "data": 'fail'}


test_data = [
    # 测试数据
    {
        "case": "用户名正确, 密码正确",
        "user": "linux超",
        "pwd": "linux超哥",
        "expected": {"code": 1001, "msg": "登录成功", "data": 'success'}
    },
    {
        "case": "用户名正确, 密码为空",
        "user": "linux超",
        "pwd": "",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": 'fail'}
    },
    {
        "case": "用户名为空, 密码正确",
        "user": "",
        "pwd": "linux超哥",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": 'fail'}
    },
    {
        "case": "用户名错误, 密码错误",
        "user": "linux",
        "pwd": "linux",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": 'fail'}
    }
]

ids = [f"测试：{data['case']}->[用户名:{data['user']}-密码:{data['pwd']}-预期:{data['expected']}]" for data in test_data]


class TestLogin(object):

    @pytest.mark.parametrize("data", test_data, ids=ids)
    def test_login(self, data):
        '''测试登录'''
        result = login(data["user"], data["pwd"])
        assert result == data["expected"]
