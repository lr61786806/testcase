import requests
import allure
import os
import pytest

from utils.HttpClient import MyHttpClient
from utils.ReadExcel import Read_Excel

# @pytest.fixture(scope='function')
# def login():
#     print("登录")
#     yield
#     print("登录完成")
#
# @allure.feature('加入购物车')
class TestCase:
    def test_1(self):
        datas = Read_Excel.read_excel('test')
        for i in range(0, len(datas)):
            print(datas[i])
            response = MyHttpClient.get(self,url=datas[i].get(3), query_dict=eval(datas[i].get(4)))
            print(response.url)
            assert response.status_code == datas[i].get(5)
    def test_2(self):
        datas = Read_Excel.read_excel('test')
        for i in range(0, len(datas)):
            print(datas[i])
            response = MyHttpClient.get(self,url=datas[i].get(3), query_dict=eval(datas[i].get(4)))
            assert response.status_code == datas[i].get(5)

if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', '../temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../temp -o ../report --clean')
