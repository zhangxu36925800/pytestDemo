from api.project import project
from core.result_base import ResultTest
from common.logger import logger

"""
该模块是把python接口封装为关键字
"""


def add_project(projectName, projectCode, status, operator, sessionId, expect_code, createTime=None):
    """
    :param projectName: 项目名称
    :param projectCode: 项目编码
    :param status: 项目状态
    :param operator:操作者
    :param createTimeime:创建时间
    :param sessionId:用户登录的sessionid
    :return:
    """

    result = ResultTest()
    playload = {
        "data":
            {"projectName": projectName, "projectCode": projectCode, "status": status, "operater": operator,
             "createTime": createTime}
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "JSESSIONID=" + sessionId
    }

    res = project.add_poject(json=playload, headers=header)
    result.success = False

    if res.status_code == 200:
        if res.json()["code"] == expect_code:
            result.success = True
            # pass
        else:
            result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    else:
        result.error = "接口请求错误,服务请求状态码【{}】, 返回信息：{} ".format(res.status_code, res)

    result.response = res
    logger.info("新增项目 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
