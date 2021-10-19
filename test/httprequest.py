import requests
import pytest
import json


class HttpRequest:
    def login_step(self):
        url = 'http://localhost:8009/api/auth/login'
        data = {"userAccount": "admin", "userPassword": "Aa123456"}
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        res = requests.post(url, json=data, headers=header)
        # print(res.json())
        # print("响应正文:", res.text)
        return res.cookies


# 登录
if __name__ == '__main__':
    cookie = HttpRequest().login_step() #获取cookies原始数据，数据类型为cookieJar
    cookie_dic = requests.utils.dict_from_cookiejar(cookie)#把cookieJar转化为字典
    print(cookie_dic['JSESSIONID'])
    url = 'http://localhost:8009/api/project/queryAllProject'
    data = {"offset": 1, "limit": 5, "data": {"projectCode": "test111"}}
    header = {'Content-Type': 'application/json;charset=UTF-8', 'Cookie': 'JSESSIONID='+cookie_dic['JSESSIONID']}
    res = requests.post(url=url, json=data, headers=header)
    print(res.json())
