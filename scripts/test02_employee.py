import json
import logging
import unittest
from parameterized import parameterized
import api
from api.api_employee import ApiEmployee
from get_location import BASE_CA
from tools.assert_common import assert_common

def get_data():
    list1 = []
    list2 = []
    with open(BASE_CA+"/data/data_test02.json")as f:
        for data in json.load(f):
            for num  in data.values():
                list1.append(num)
            list2.append(list1)

        return list2


class Employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()
    @parameterized.expand(get_data())
    def test_01_post(self,username,mobile,workNumber):
        r = self.api.post_user(username,mobile,workNumber)
        print("添加员工返回的响应信息:{}".format(r.json()))
        logging.info("添加员工返回的响应信息:{}".format(r.json()))

        api.user_id = r.json().get("data").get("id")
        print("新增员工的id为:{}".format(api.user_id))
        logging.info("新增员工的id为:{}".format(api.user_id))

        #断言
        assert_common(self,r)

    def test_02_get(self):
        r = self.api.get_user()
        print("查询添加的员工的信息:{}".format(r.json()))
        logging.info("查询添加的员工的信息:{}".format(r.json()))

        # 断言
        assert_common(self, r)


    def test_03_put(self,username="TTSS111"):
        r = self.api.put_user(username)

        print("修改员工的信息:{}".format(r.json()))
        logging.info("修改员工的信息:{}".format(r.json()))
        # logging.info("修改员工的信息:{}".format(r.json()))


        # 断言
        assert_common(self,r)

    def test_04_delete(self):
        r = self.api.delete_user()
        print("删除员工返回的响应信息:{}".format(r.json()))
        logging.info("删除员工返回的响应信息:{}".format(r.json()))

        # 断言
        assert_common(self, r)

