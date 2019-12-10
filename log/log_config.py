# 导包
import logging
# 初始化日志配置
# 创建日志方法
from get_location import BASE_CA


def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
   # 设置日志级别
    logger.setLevel(logging.INFO)

   # 创建处理器(输出到控制台)
   #  shl =  logging.StreamHandler()

   #创建处理器(输出到文件)
    trfhl =logging.FileHandler(filename=BASE_CA+"/log/log_01.log",encoding="utf-8")
   # 创建格式化器
    fmter = logging.Formatter(fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")

    # 将格式化器添加到处理器
    # shl.setFormatter(fmter)

    trfhl.setFormatter(fmter)
   # 将处理器添加到日志器
   #  logger.addHandler(shl)
    logger.addHandler(trfhl)