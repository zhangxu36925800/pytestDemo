<<<<<<< HEAD
@echo off
call D:
call cd D:\Document\pycharmworkspace\pytestDemo\testcases\api_test
call allure generate ./report/ -o D:\Document\pythonreport --clean
call cd D:\Document&&allure open pythonreport
=======
@echo off
call E:
call cd E:\document\pycharm-workspace\pytestdemo\testcases\api_test
call allure generate ./report/ -o E:\document\pythonreport --clean
call cd E:\document&&allure open pythonreport
>>>>>>> origin/master
pause