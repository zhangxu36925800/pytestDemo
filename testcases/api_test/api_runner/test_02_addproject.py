import pytest
import allure
import jsonpath
from operation.project import add_project
from operation.project import query_project_unino
from testcases.conftest import api_data
from common.project_path import api_root_url
from common.logger import logger
from common.time_operate import TimeUtil
from common.assert_utill import AssertUtil


# @allure.step("步骤2 ==>> 新建项目")
# def step_1(username):
#     logger.info("步骤1 ==>> 登录用户：{}".format(username))
@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
class TestAddProject():
    # @allure.story("这是用户故事")
    @allure.feature("新增项目模块")
    @allure.tag(api_root_url + "api/project/editProject")
    @allure.title("用例--新增项目")
    @allure.description("接口请求地址:" + api_root_url + "/api/project/editProject")
    @pytest.mark.parametrize("projectName,projectCode,status,operater,expect_code,expect_msg",
                             api_data["test_add_project"])
    @pytest.mark.usefixtures("add_delete_project")
    @pytest.mark.test2
    def test_add_project(self, login_fixture, projectName, projectCode, status, operater, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        user_cookie = login_fixture  # 获取登录时产生的cookie
        current_time = TimeUtil.format_timer_to_str()  # 获取当前时间(24hours)
        res = add_project(projectName, projectCode, status, operater, user_cookie, createTime=current_time)
        globals().setdefault("codeNo", res.json()["codeNo"])
        if res.status_code == 200:
            AssertUtil.assert_equal(res, expect_code, res.json()["code"])  # 断言返回编码
            AssertUtil.assert_str(res, expect_msg, res.json()["msg"])  # 断言返回消息
            # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(expect_msg, res.json()))
        else:
            AssertUtil.assert_equal(res, 200, res.status_code)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(expect_code, res.json()))

    # def get_global(self):
    #     param_list = []
    #     expect_codeno = globals().get("codeNo")
    #     param_list.append(expect_codeno)
    #     return param_list
    @allure.feature("查询新增项目")
    @allure.tag(api_root_url + "api/project/queryAllProject")
    @allure.title("用例--查询新增项目")
    @allure.description("接口请求地址:" + api_root_url + "/api/project/queryAllProject")
    def test_query_poject(self, login_fixture):
        # 获取全局变量(上一个接口的返回值codeNo)
        expect_codeno = globals().get("codeNo")
        user_cookie = login_fixture  # 获取登录时产生的cookie
        res = query_project_unino(expect_codeno, user_cookie)
        actual_codeNo = jsonpath.jsonpath(res.json(), '$..projectCode')[0]  # gain the value of 'projectCode' in the response above
        # actual_codeNo= res.json()["rows"][0].get("projectCode")
        AssertUtil.assert_equal(res, expect_codeno, actual_codeNo)  # 断言查到的项目编码是否和新增的一致
        # logger.info("我是全局变量项目编码:{}".format(expect_codeNo))

if __name__ == "__main__":
    pytest.main(["-q", "-s", "test_02_addproject.py"])
