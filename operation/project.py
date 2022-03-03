from api.project import project
from core.result_base import ResultTest

# from common.logger import logger

"""
该模块是把python接口封装为关键字
"""


def add_project(projectName, projectCode, status, operator, sessionId, createTime=None):
    """
    :param projectName: 项目名称
    :param projectCode: 项目编码
    :param status: 项目状态
    :param operator:操作者
    :param createTimeime:创建时间
    :param sessionId:用户登录的sessionid
    :return:
    """

    # result = ResultTest()
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
    return res


def query_project_unino(projectCode, sessionId):
    """
    根据项目编码查找指定项目
    :param projectCode:  项目编码
    :param sessionId: 用户登录cookie
    :return:
    """
    playload = {"offset": 1, "limit": 100, "data": {"projectCode": projectCode}}
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "JSESSIONID=" + sessionId
    }
    res = project.query_project(json=playload, headers=header)
    return res


