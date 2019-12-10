import api
import requests

class ApiEmployee:
    def __init__(self):
        self.url_add = api.BASE_URL +  "/api/sys/user"
        self.url_employee = api.BASE_URL + "/api/sys/user/{}"

    def post_user(self,username,mobile,workNumber):
        data = {"username":username,"mobile":mobile,"workNumber":workNumber}
        return  requests.post(url= self.url_add,json=data,headers=api.headers)

    def get_user(self,):
        return  requests.get(url=self.url_employee.format(api.user_id),headers=api.headers)

    def put_user(self,username):
        data = {"username":username}
        return  requests.put(url=self.url_employee.format(api.user_id),json=data,headers=api.headers)

    def delete_user(self,):
        return  requests.delete(url=self.url_employee.format(api.user_id),headers=api.headers)


