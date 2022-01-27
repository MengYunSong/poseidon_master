# coding=utf-8

"""
@author:songmengyun
@file: gen_code_json.py
@time: 2019/06/04

"""

import os
import logging
import getpass
from datetime import datetime
from functools import reduce
from .base_obj import CodeGeneratorResp


def generator_obj(file_path, file_name, data_json=None, resp_json=None, db_json=None, keep_value=False):
    """

    :param file_path: 对象存放路径，绝对路径
    :param file_name: .py文件名称，后面会根据该名称创建类名
    :param data_json: 需要转为类的请求json
    :param resp_json: 需要转为类的返回json
    :param db_json:  需要转为类的dbjson
    :param keep_value: 如果为True，会赋json中值；如果为False，默认为None
    :return:以file_path为路径，file_name为名的.py文件，该文件中会有data/resp/db 3个类
    """
    # dir = os.getcwd()   # 获取当前路径
    # dir_path = os.path.join(dir , 'data_obj')
    # obj_dir_path = os.path.join(dir_path, '%s.py' % (py_file_name))
    # if not os.path.exists(dir_path):
    #     try:
    #         os.mknod(dir_path)
    #     except Exception as e:
    #         logging.info(e)

    obj_dir_path = os.path.join(file_path, '%s.py' % (file_name))

    title_sample = '''
# coding=utf-8

"""
@author:{0}
@file: {1}.py
@time: {2}

"""

'''.format(getpass.getuser(), py_file_name, datetime.now())
    with open(obj_dir_path, 'w') as f:
        f.write(title_sample)
        f.write('\n')

    class_name_list = py_file_name.split('_') if '_' in py_file_name else py_file_name
    class_name_upper = [x.capitalize() for x in class_name_list if x.istitle() == False]
    # class_name_upper = list(map(lambda x:x.capitalize(),class_name_list))
    name = ''
    for x in class_name_upper:
        name += x
    data_class_name = name + 'Data'
    resp_class_name = name + 'Resp'
    db_class_name = name + 'DB'
    if data_json:
        data_obj = CodeGeneratorResp(resp=data_json, root_name=data_class_name, keep_value=keep_value)
        data_class_list = data_obj.gen_code()
        with open(obj_dir_path, 'a+') as f:
            for x in data_class_list:
                f.write(x)
                f.write('\n')
            f.write('\n')
    if resp_json:
        resp_obj = CodeGeneratorResp(resp=resp_json, root_name=resp_class_name, keep_value=keep_value)
        reps_class_list = resp_obj.gen_code()
        with open(obj_dir_path, 'a+') as f:
            for x in reps_class_list:
                f.write(x)
                f.write('\n')
            f.write('\n')
    if db_json:
        db_obj = CodeGeneratorResp(resp=db_json, root_name=db_class_name, keep_value=keep_value)
        db_class_list = db_obj.gen_code()
        with open(obj_dir_path, 'a+') as f:
            for x in db_class_list:
                f.write(x)
                f.write('\n')
            f.write('\n')

    send_sample = '''

class {0}():
    def __init__(self, data=None, resp=None, db=None):
        self.method = ''
        self.url = ''
        self.data = data
        self.headers = ''
        self.resp = resp
        self.db = db

    def send_request_then_check(self, http_status_exp=200, status_exp=0, is_db_check=False):
        pass

    '''.format(name)
    with open(obj_dir_path, 'a+') as f:
        f.write(send_sample)
        f.write('\n')




if __name__ == '__main__':
    py_file_path = '/Users/songmengyun/automation_NC/business/bus_abs/'  # 文件目录的绝对路径
    py_file_name = 'abs_msg_temlpate'   # .py文件名称，后面类名会基于该名称命名
    data_json = {
        "templateId": 1,
        "audience": {
            "uid": [
                1,
                2,
                3
            ],
            "contentArgs": {
                "key1": "同学",
                "key2": "你好",
                "key3": "你妈妈喊你回家吃饭了"
            }
        }
    }
    resp_json = {
        "data": 636571924722221056,
        "message": "success",
        "status": 0,
        "time": None
    }

    db_json = {}
    generator_obj(py_file_path, py_file_name, data_json, resp_json)
