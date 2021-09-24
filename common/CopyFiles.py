import os  # os是用来切换路径和创建文件夹的
from shutil import copy  # shutil 是用来复制黏贴文件的
class CopyFiles:
    def EvromentConfig(self):
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取当前文件的绝对路径
        data_file_path = os.path.join(BASE_PATH, "config", "environment.properties")  # 获取要copy文件的目录
        newpath = os.path.join(BASE_PATH, "testcases/api_test/report")  # 获取要存放的目标路径
        copy(data_file_path, newpath)  # copy文件至目标路径l


if __name__=='__main__':
    CopyFiles().EvromentConfig()