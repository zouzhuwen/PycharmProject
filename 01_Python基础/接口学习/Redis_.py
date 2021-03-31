# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Time  : 2019/8/5 0005 16:04
import redis
from common.LogInfo import logger
def del_redis(name,host='192.168.203.211', port=7001,password='',db=0):
    try:
        r = redis.Redis(host=host, port=port,password=password,db=db)
        a=(r.keys(name)) #获取
        logger.info("清除前为：%s"%a)
        for key in a:
            r.delete(key)
        logger.info("清除后为：%s"%r.keys(name))
        return r
    except Exception as e:
        logger.error("redis连接失败：%s"%e)
        return False
if __name__ == '__main__':
    pass