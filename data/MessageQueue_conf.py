#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-21
"""

from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env



class MessageQueue_conf:
    @property
    def uc_mq_hujiang_receive(self):
        # 发送接收配置
        return cb.get_value_from_env_data_dict({
            Env.qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 15672,
                         "vhost": "pass", "queue": "pass.league.q.test"},
        })

    @property
    def uc_mq_hujiang_send(self):
        # 发送消息配置
        return cb.get_value_from_env_data_dict({
            Env.qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 5672,
                         "vhost": "pass", "exchange": "f.pass.ex", "routingKey": ""},
        })

    @property
    def uc_mq_hujiang_admin(self):
        # 发送管理消息通道配置
        return cb.get_value_from_env_data_dict({
            Env.qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 15672,
                         "vhost": "pass", "queue": "pass.league.q.test"},
        })

    @property
    def uc_mq_cc_receive(self):
        # 发送接收配置
        return cb.get_value_from_env_data_dict({
            Env.qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 5672,
                         "vhost": "pass", "queue": "pass.league.cc.q"},
        })

    @property
    def uc_mq_cc_send(self):
        # 发送消息配置
        return cb.get_value_from_env_data_dict({
            Env.qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 5672,
                         "vhost": "pass", "exchange": "base.pass.cc.default.ex", "routingKey": ""},
        })

    @property
    def uc_mq_cc_admin(self):
        # 发送管理消息通道配置
        return cb.get_value_from_env_data_dict({
            Env.qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 15672,
                         "vhost": "pass", "queue": "pass.league.cc.q"},
        })

messageQueueConf = MessageQueue_conf()
