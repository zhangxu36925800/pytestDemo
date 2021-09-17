import requests


class HttpRequest:
    def http_reques(self, url, data):
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        res = requests.post(url, json=data, headers=header)
        print(res.json())
        print("响应正文:", res.text)
        # print("响应头:", res.headers)
        # print("请求头:", res.request.headers)
        # print("sessionKey:",res.jso
        return res


# 登录
if __name__ == '__main__':
    url = 'http://localhost:8009/api/auth/login'
    data = {"userAccount": "admin", "userPassword": "Aa123456"}
    res = HttpRequest().http_reques(url, data)
    print("哈哈哈:")
