#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-21
"""

from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env


class Memcache_conf:
    @property
    def uc_memcache(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: [('192.168.36.212', 11211), ('192.168.36.212', 11212)],
        })

    @property
    def uc_memcache_cc(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: [('192.168.36.212', 11211), ('192.168.36.212', 11212)],
        })
memcache_conf = Memcache_conf()
