@echo off
call D:
call cd D:\Document\pycharmworkspace\pytestDemo\testcases\api_test
call allure generate ./report/ -o D:\Document\pythonreport --clean
call cd D:\Document&&allure open pythonreport
pause