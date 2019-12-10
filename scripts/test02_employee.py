import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class Employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()

    def test_01_post(self,username="TTSS",mobile="13811113333",workNumber="123654987"):
        r = self.api.post_user(username,mobile,workNumber)
        print("执行后返回的响应信息",r.json())
        api.user_id = r.json().get("data").get("id")
        print("新增员工的id为",api.user_id)
        assert_common(self,r)

    def test_02_get(self):
        r = self.api.get_user()
        print("查询添加的员工信息",r.json())
        assert_common(self, r)


    def test_03_put(self,username="TTSS01"):
        r = self.api.put_user(username)
        print("修改员工的信息",r.json())
        assert_common(self, r)






    def test_04_delete(self):
        r = self.api.delete_user()
        print("删除员工返回的响应信息",r.json())
        assert_common(self, r)

