@echo off
call D:
call cd D:\Document\pycharmworkspace\pytestDemo\run
call allure generate ./report/ -o D:\Document\pythonreport --clean
call cd D:\Document&&allure open pythonreport
