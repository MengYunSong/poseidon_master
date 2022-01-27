# coding=utf-8

"""
@author:songmengyun
@file: base_obj.py
@time: 2019/06/03

"""
import logging
import decimal
from enum import Enum
import copy

"""操作对象的所有方法"""

class BaseObj(object):

    def __init__(self, dict_attributes=None, **kwargs):
        """origin doc"""
        self.update_value(dict_attributes)

    def get_all_attr(self, obj):
        """获取对象或者类的所有属性、方法"""
        if obj:
            return dir(obj)

    def if_value_exist(self, obj, attribute=None):
        """判断一个对象或类是否有指定的属性或方法"""
        try:
            hasattr(obj, attribute) == True
        except Exception as e:
            logging.error(e)
            raise Exception

    def update_value(self, dict_attributes=None, **kwargs):
        """更新类或对象的属性值"""
        if dict_attributes is None:
            dict_attributes = kwargs
        else:
            dict_attributes.update(kwargs)
        if dict_attributes:
            for attribute_name in dict_attributes.keys():
                setattr(self, attribute_name, dict_attributes.get(attribute_name))

    def get_attr_value(self, obj, attr, default=None):
        """获取对象属性"""
        value = getattr(obj, attr, default)
        if value is None:
            return default
        else:
            return value

    def del_value(self):
        """删除类或对象的所有属性"""
        for k, v in vars(self).items():
            setattr(self, k, None)

    def del_attr_batch(self, obj, attr_list):
        """
        批量删除属性
        :param attr_list:属性名称列表
        :return:None
        """
        if isinstance(obj, list):
            for index in range(len(obj)):
                list(map(lambda x: delattr(obj[index], x), attr_list))
        else:
            list(map(lambda x: delattr(obj, x), attr_list))

    def set_attr_value_batch(self, obj, attr_list, value):
        """
        批量设置属性
        :param attr_list:属性名称列表
        :return:None
        """
        if isinstance(obj, list):
            for index in range(len(obj)):
                list(map(lambda x: setattr(obj[index], x, value), attr_list))
        else:
            list(map(lambda x: setattr(obj, x, value), attr_list))

    def get_attr_value_batch(self, obj, attr_list, miss_value=None):
        """
        批量获取属性
        :param attr_list:属性名称列表
        :param miss_value:默认值
        :return:属性值对应列表
        """
        value_list = []
        for attr in attr_list:
            value = getattr(obj, attr, miss_value)
            value_list.append(value)
        return value_list

    def attr_rename(self, obj, old_name, new_name, is_delete=False):
        """
        属性重命名
        :param obj: 对象
        :param old_name: 旧的属性名称
        :param new_name: 新的属性名称
        :param is_delete: 是否删除旧的属性
        :return:
        """
        if hasattr(obj, old_name):
            setattr(obj, new_name, getattr(obj, old_name))
            if is_delete:
                delattr(obj, old_name)
            else:
                pass
        else:
            return False

    def attr_move(self, obj, target_name, newobj, new_name=None, is_delete=False):
        """
        移除属性
        :param obj: 对象
        :param old_name: 旧的属性名称
        :param new_name: 新的属性名称
        :param is_delete: 是否删除旧的属性
        :return:
        """
        if hasattr(obj, target_name):
            if new_name:
                setattr(newobj, new_name, getattr(obj, target_name))
            else:
                setattr(newobj, target_name, getattr(obj, target_name))

            if is_delete:
                delattr(obj, target_name)
            else:
                pass
        else:
            return False
base_obj = BaseObj()

class CodeGeneratorResp(object):
    """
    对返回值中嵌套的dict、list中的dict、嵌套多层的dict自动在结构位置生成一个子类
    子类名称为大写的字段名，如字段名已s结尾，则去除s，如字段名为detailProducts，生成的类名为DetailProduct
    使用方法：
    初始化类，调用gen_code方法
    """
    def __init__(self, resp, root_name="Root", keep_value=False):
        """
        :param resp: json格式内容
        :param root_name: 生成的类名，默认为Root
        :param keep_value: 是否依照resp给生成的类属性赋默认值，默认为False，即生成的类属性值均为None
        """
        self.resp = resp
        self.root_name = root_name
        self.keep_value = keep_value

    def gen_code(self):
        out = []
        tab = 4
        out.append("class %s():" % self.root_name)
        out.append(" " * tab + "def __init__(self):")
        # out.append(" " * (tab*2) + "super().__init__")
        if isinstance(self.resp, list):
            out.append(" " * (tab + 4) + "self.root = []")
            out.append("\r")
            out.append(" " * tab + "class Root(object):")
            out.append(" " * (tab + 4) + "def __init__(self):")
            out += self._gen_dict(self.resp[0], tab=(tab + 8))
        elif isinstance(self.resp, dict):
            out += self._gen_dict(self.resp, tab=8)
        # a = open("d:/aaa.txt", "w")
        for line in out:
            print(line)
            # aa=line
            # a.write(aa)
            # a.write("\n")

        return out

    def _gen_dict(self, src_dict, tab):
        out = []
        multi = []
        for k, v in list(dict(src_dict).items()):
            if self.keep_value is True and isinstance(v, (dict, list)) is False:
                if isinstance(v, str):
                    v = '''"%s"''' % v
                out.append(" " * tab + "self.%s = %s" % (k, v))
            else:
                out.append(" " * tab + "self." + k + " = None")
            if isinstance(v, (dict, list)):
                multi.append(k)
        out.sort()
        tab -= 4
        for k in multi:
            v = src_dict.get(k)
            out.append("\r")
            out.append(" " * tab + "class " + str(k[0].upper() + k[1:]).rstrip("s") + "():")
            out.append(" " * (tab + 4) + "def __init__(self):")
            # out.append(" " * (tab + 8) + "super().__init__")
            if isinstance(v, dict):
                out += self._gen_dict(v, tab=tab + 8)
            if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                out += self._gen_dict(v[0], tab=tab + 8)
        return out









