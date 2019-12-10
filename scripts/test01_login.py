import json
import logging
import unittest
from parameterized import parameterized
import api
from api.api_login import ApiLogin
from get_location import BASE_CA
from tools.assert_common import assert_common

def get_data():
    list1 = []
    list2 = []
    with open(BASE_CA+"/data/data_test01.json")as f:
        for data in json.load(f):
            for num  in data.values():
                list1.append(num)
            list2.append(list1)

        return list2






class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取Apilogin   对象
        cls.login = ApiLogin()

        #数据驱动 参数化

    @parameterized.expand(get_data())
    # 登录测试方法
    def test01_login(self,mobile,password):
        # 调用业务方法
        r = self.login.api_login(mobile,password)

        token = r.json().get("data")
        api.headers['Authorization'] = "Bearer " + token

        #数据收集
        print("登录成功组合后的token:{}".format(api.headers))
        logging.info("登录成功组合后的token:{}".format(api.headers))

        print("登录返回的数据:",r.json())
        logging.info("登录返回的数据:{}".format(r.json()))

        print("登录成功后headers值为:{}".format(api.headers))
        logging.info("登录成功后headers值为:{}".format(api.headers))
        # 断言
        assert_common(self,r)

