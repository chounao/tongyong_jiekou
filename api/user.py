import os
from core.rest_client import RestClient
from common.read_data import  data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH,"config.ini")
HTTP_data = data.load_ini(data_file_path)['HTTP']
api_root_url = HTTP_data['api_url']
work_url = HTTP_data['work_url']
saas_url =  HTTP_data['saas_url']

class User(RestClient):


    def __init__(self,api_root_url,**kwargs):
        super(User,self).__init__(api_root_url, **kwargs)

    def login(self,**kwargs):

        return self.post('/loginAccount.do',**kwargs)


user = User(api_root_url)