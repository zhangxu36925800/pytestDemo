import pytest
from common.project_path import BASE_PATH
from run.pytestiniconfig import test_getinicase
def test_run_case():
    ret = test_getinicase()
    ret.append(BASE_PATH+"/testcases/api_test/api_runner")
    pytest.main(ret)
if __name__ == "__main__":
    test_run_case()
    # pytest.main(["-q","-s","case_run.py"])