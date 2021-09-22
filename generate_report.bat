@echo off
call E:
call cd E:\document\pycharm-workspace\pytestdemo\testcases\api_test
call allure generate ./report/ -o E:\document\pythonreport --clean
call cd E:\document&&allure open pythonreport
pause