import os
from common.read_data import data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #获取当前文件所在的项目根目录
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini") #根据项目的根目录获取setting.ini的绝对路径
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
mysql_data = data.load_ini(data_file_path)["mysql"]
