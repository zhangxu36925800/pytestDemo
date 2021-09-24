import pytest
import allure
from operation.user import login_user
from testcases.conftest import api_data
from common.project_path import api_root_url
from common.logger import logger
from common.CopyFiles import CopyFiles

@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():
    @allure.tag(api_root_url+"/api/auth/login")
    @allure.title("用例--登录用户")
    @allure.description("接口请求地址:"+api_root_url+"/api/auth/login")
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_user(username, password)
        step_1(username)
        assert result.response.status_code == except_code
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        # logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "test_03_login.py"])
CopyFiles().EvromentConfig()

