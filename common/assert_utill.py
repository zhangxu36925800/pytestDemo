from common.logger import logger
from core.result_base import ResultTest
import pytest


class AssertUtil(object):
    # def compare_json(excepted_json, actual_json, msg=None):
    #     # l.info("比较期待的json结果与实际json结果是否一致")
    #     if excepted_json == {} and actual_json != {}:
    #         AssertUtil.assert_equal(excepted_json, actual_json)
    #     if actual_json == {} and excepted_json != {}:
    #         AssertUtil.assert_equal(excepted_json, actual_json)
    #
    #     for key in excepted_json.keys():
    #         # 考虑值是否是dict
    #         if isinstance(excepted_json[key], dict):
    #             AssertUtil.compare_json(excepted_json[key], actual_json[key])
    #             break
    #
    #         # TODO 还需考虑值是list的情况
    #         if isinstance(excepted_json[key], list):
    #             continue
    #         try:
    #             assert excepted_json[key] == actual_json[key]
    #         except Exception as ex:
    #             # result.error=("期待的json({0})与实际的json({1})不一致, 不同值的key:{2}, msg:{3}".format(excepted_json, actual_json, key, msg))
    #             raise Exception(
    #                 "compare failed, excepted:{0}, actual:{1}, msg:{2}".format(excepted_json, actual_json, msg))
    @staticmethod
    def __convert_byte_str(b):
        if isinstance(b, bytes):
            return b.decode()
        return b

    @staticmethod
    def assert_equal(res, expected, actual): #校验非文本字符类型的数据
        if res.status_code == 200:
            expected = AssertUtil.__convert_byte_str(expected)
            actual = AssertUtil.__convert_byte_str(actual)
            assert expected == actual, "期望结果:【{}】, 实际结果:【{}】,响应结果:{} ".format(expected,actual,res.json())
        else:
            assert res.status_code == 200,"接口请求错误,服务请求状态码【{}】, 返回信息：{} ".format(res.status_code, res)

    @staticmethod
    def assert_str(res,expect_str,actual_str):#校验包含文本字符类型的数据
        if res.status_code == 200:
            expect_str = AssertUtil.__convert_byte_str(expect_str)
            actual_str = AssertUtil.__convert_byte_str(actual_str)
            assert expect_str in actual_str, "期望结果:【{}】, 实际结果:【{}】,响应结果:{} ".format(expect_str,actual_str,res.json())
        else:
            assert res.status_code == 200, "接口请求错误,服务请求状态码【{}】, 返回信息：{} ".format(res.status_code, res.json())

