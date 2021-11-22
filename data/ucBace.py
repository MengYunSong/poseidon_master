from poseidon.base import CommonBase as cb
from poseidon.base.Env import Env


#######################
# 用户中心redis配置
#######################

class UcBase(object):
    @property
    def uc_redis_hujiang_busi_cache(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env. qa: {"host":"192.168.36.212", "port":"1012","db":0},
    })

    @property
    def uc_redis_hujiang_db_cache(self):
        # 数据库缓存
        return cb.get_value_from_env_data_dict({
            Env. qa: {"host":"192.168.36.212", "port":"1031","db":0},
    })

    @property
    def uc_redis_cc_busi_cache(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env. qa: {"host": "192.168.36.212", "port": "1033", "db": 0},
        })

    @property
    def uc_redis_cc_db_cache(self):
        # 数据库缓存
        return cb.get_value_from_env_data_dict({
            Env. qa: {"host": "192.168.36.212", "port": "1034", "db": 0},
        })

    @property
    def uc_redis_wechat_busi_cache(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: {"host": "192.168.36.212", "port": "1035", "db": 0},
        })

    @property
    def uc_redis_wechat_db_cache(self):
        # 数据库缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: {"host": "192.168.36.212", "port": "1036", "db": 0},
        })

    @property
    def uc_redis_wechat_db1_cache(self):
        # 数据库缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: {"host": "192.168.36.212" , "port": "1036" , "db": 1} ,
        })


#######################
# 用户中心memcache配置
#######################

    @property
    def uc_memcache_hujiang(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: [('192.168.36.212', 11211), ('192.168.36.212', 11212)],
    })

    @property
    def uc_memcache_cc(self):
        # 业务缓存
        return cb.get_value_from_env_data_dict({
            Env.qa: [('192.168.36.212', 11213), ('192.168.36.212', 11214)],
    })



#######################
# 用户中心mq配置
#######################

    @property
    def uc_mq_hujiang_receive(self):
        # 发送接收配置
        return cb.get_value_from_env_data_dict({
            Env. qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 5672,"vhost": "pass", "queue": "pass.league.q.test"},
    })

    @property
    def uc_mq_hujiang_send(self):
        # 发送消息配置
        return cb.get_value_from_env_data_dict({
            Env. qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75","port": 5672, "vhost": "pass", "exchange": "f.pass.ex","routingKey":""},
    })

    @property
    def uc_mq_hujiang_admin(self):
        # 发送管理消息通道配置
        return cb.get_value_from_env_data_dict({
            Env. qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75","port": 15672, "vhost": "pass", "queue": "pass.league.q.test"},
    })



    @property
    def uc_mq_cc_receive(self):
        # 发送接收配置
        return cb.get_value_from_env_data_dict({
            Env. qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75", "port": 5672,"vhost": "pass", "queue": "pass.league.cc.q"},
    })

    @property
    def uc_mq_cc_send(self):
        # 发送消息配置
        return cb.get_value_from_env_data_dict({
            Env. qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75","port": 5672, "vhost": "pass", "exchange": "base.pass.cc.default.ex", "routingKey":""},
    })

    @property
    def uc_mq_cc_admin(self):
        # 发送管理消息通道配置
        return cb.get_value_from_env_data_dict({
            Env. qa: {"username": "ha_user", "password": "ha_user", "server": "192.168.36.75","port": 15672, "vhost": "pass", "queue": "pass.league.cc.q"},
    })

uc_base = UcBase()
