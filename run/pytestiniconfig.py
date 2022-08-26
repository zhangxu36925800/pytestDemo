import pytest
from common.read_data import data
from common.project_path import data_file_path


def test_getinicase():
    mode_case = data.load_ini(data_file_path)["mode"]
    ret = ["-q","-s","-m"]
    for key in mode_case.keys():
        if mode_case[key] == "1":
            ret.append(key)
    return ret
    # print(mode_case)
    # return mode_case


if __name__ == "__main__":
    # pytest.main(["-s", "pytestiniconfig.py"])
    ret = test_getinicase()
    print(ret)
