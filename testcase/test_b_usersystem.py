import json
import os
import sys

# 引入的模块路径，就能找到自定义模块了
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Yaml import getYaml
import requests
import jsonpath
import pytest
from logfile import logclass

logdata = logclass.logger()


class Test_usersystem():

    # 类前置获取所有参数
    @classmethod
    def setup_class(cls):
        logdata.info('========#进入 test_a_codeloginToken.py=======')
        logdata.info('\n======Start个人信息场景Test_usersystem类用例执行开始======')
        global url, token, userid, headerJson
        logdata.info('\n======setup_class前置方法global参数提取======')
        url = getYaml.getYamlValue('URL')
        token = getYaml.getYamlValue('token')
        userid = getYaml.getYamlValue('userid')
        headerJson = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "authorization": token
        }
        logdata.info('\n======setup_class前置方法global参数提取完成======')

    # 类后置方法
    @classmethod
    def teardown_class(cls):
        logdata.info('\n======Over个人信息场景Test_usersystem类用例执行完成======')

    def test_usersid(self):
        logdata.info('\n======进入test_usersid接口，获取个人信息=====')
        # print(token)
        # print(userid)
        test_login_url = (url + '/openapi/usersystem/info/' + userid)
        # print(test_login_url)
        r = requests.get(test_login_url, headers=headerJson)
        # 输出返回值
        logdata.info("codelogin接口返回值：" + "\n" + json.dumps(r.json(), ensure_ascii=False))
        # 断言
        assert r.json()["msg"] == "操作成功"
        logdata.info("\n=======test_usersid接口执行结束")

    @pytest.mark.xfail(reason='该功一天只能执行一次')
    # @pytest.mark.skip  #无条件跳过
    def test_birthday(self):
        logdata.info('\n======进入test_birthday接口，修改生日=====')
        test_login_url = (url + '/openapi/usersystem/info/birthday')
        datajson = json.dumps({"userId": userid, 'birthday': "1996-12-24"})
        r = requests.post(test_login_url, headers=headerJson, data=datajson)
        # 输出返回值
        logdata.info("codelogin接口返回值：" + "\n" + json.dumps(r.json(), ensure_ascii=False))
        # 断言一天之内修改一次，用codestat判断
        # assert r.json()["msg"] == "操作成功"
        assert r.status_code == 200
        logdata.info("\n=======test_birthday接口执行结束")
