#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env


class Db_conf:
    @property
    def HJ_PassportSqlAlchemyStrMySQL(self):
        return cb.get_value_from_env_data_dict({
            Env.qa: "mysql+mysqldb://user_pass:user_pass_123@192.168.38.92:3306/HJ_Passport?charset=utf8",
        })


dbconf = Db_conf()
