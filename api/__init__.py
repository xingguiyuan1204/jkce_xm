# 测试服务器ip地址
from log.log_config import init_log_config

BASE_URL = "http://182.92.81.159"
headers = {"Content-Type":"application/json"}
user_id = None


#放到页面基类__init__里
# 启用日志配置

#调用函数
init_log_config()