import pytest
import allure
from operation.project import add_project
from testcases.conftest import api_data
from common.project_path import api_root_url
from common.logger import logger
from common.time_operate import TimeUtil
from common.assert_utill import AssertUtil


# @allure.step("步骤2 ==>> 新建项目")
# def step_1(username):
#     logger.info("步骤1 ==>> 登录用户：{}".format(username))
@allure.tag(api_root_url + "/api/auth/login")
@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("新增项目模块")
class TestAddProject():

    # @allure.story("这是用户故事")
    @allure.title("用例--新增项目")
    @allure.description("接口请求地址:" + api_root_url + "/api/project/editProject")
    @pytest.mark.parametrize("projectName,projectCode,status,operater,expect_code,expect_msg",
                             api_data["test_add_project"])
    @pytest.mark.usefixtures("add_delete_project")
    def test_add_project(self, login_fixture, projectName, projectCode, status, operater, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        user_cookie = login_fixture  # 获取登录产生的cookie
        current_time = TimeUtil.format_timer_to_str()  # 获取当前时间(24hours)
        res = add_project(projectName, projectCode, status, operater, user_cookie, createTime=current_time)
        if res.status_code == 200:
            AssertUtil.assert_equal(res, expect_code, res.json()["code"])#断言返回编码
            AssertUtil.assert_str(res,expect_msg,res.json()["msg"]) #断言返回消息
            # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(expect_msg, res.json()))
        else:
            AssertUtil.assert_equal(res,200,res.status_code)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(expect_code, res.json()))


if __name__ == "__main__":
    pytest.main(["-q", "-s", "test_02_addproject.py"])
