from core.rest_client import RestClient
from common.project_path import api_root_url
#继承父类，重写接口请求,封装Http接口为python接口
class Project(RestClient):
    def __init__(self,api_root_url,**kwargs):
        super(Project,self).__init__(api_root_url,**kwargs)

    def add_poject(self,**kwargs):
       return self.post("/api/project/editProject",**kwargs) #重写post方法


project = Project(api_root_url)