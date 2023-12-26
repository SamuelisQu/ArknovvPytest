import pytest
import json
import os
import sys

# 引入的模块路径，就能找到自定义模块了
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Yaml import getYaml
import requests
import jsonpath

# from logging import log
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# logger_dir=os.path.dirname(os.path.abspath(__file__))
# sys.path.append(logger_dir)
from logfile import logclass

# print(BASE_DIR)
# print(os.path.dirname(os.path.abspath(__file__)))
logdata = logclass.logger()


class TestUserTasks():
    # 类前置获取所有参数
    @classmethod
    def setup_class(cls):
        logdata.info('======进入test_a_codeloginToken.py========')
        # print('\n======Start登录场景TestUserTasks类用例执行开始======')
        logdata.info('\n======Start登录场景TestUserTasks类用例执行开始======')
        global url, phone, code, headerJson
        # print('\n======setup_class前置方法global参数提取======')
        logdata.info('\n======setup_class前置方法global参数提取======')

        url = getYaml.getYamlValue('URL')
        phone = getYaml.getYamlValue('phone')
        code = getYaml.getYamlValue('code')
        headerJson = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8"}
        logdata.info('\n======setup_class前置方法global参数提取完成======')

    # 类后置方法
    @classmethod
    def teardown_class(cls):
        logdata.info('\n======Over登录场景TestUserTasks类用例执行完成======')

    # 声明下面是一个任务
    # pytest.mark.run(order=2)设置用例执行的顺序
    # @pytest.mark.run(order=1)
    def test_login(self):
        logdata.info('\n======进入testlogin接口，获取短信验证码=====')
        test_login_url = (url + "/openapi/usersystem/sms/send")
        # print(tets_login_url)
        # 字段转换成str
        datajson = json.dumps({"phone": phone, "type": "0"})
        # print(type(datajson))
        r = requests.post(test_login_url, headers=headerJson, data=datajson)
        # 拼接时吧字段装换成字符串再进行拼接
        logdata.info("send接口返回值：" + json.dumps(r.json(), ensure_ascii=False))
        # 断言
        assert r.json()["msg"] == "操作成功"

        # 返回值先使用dumps装换成str,再用loads装换成字典，字典在后面能根据valus取key的值
        # json_dict = json.loads((json.dumps(response.json(), ensure_ascii=False)))
        # 判断成功或者失败
        # if response.json()["msg"] == "操作成功":
        #     response.success("请求成功")
        # else:
        #     response.status_code
        # 第二种判断法方式
        # if r.status_code != 200:
        #     r.success("请求成功")
        # else:
        #     r.status_code
        # json.dumps方法时加入ensure_ascii=False参数，这样可以使中文字符串按原样输出
        # print(json.dumps(r.json(),ensure_ascii = False))
        logdata.info('\n======testlogin接口结束=====')

    # 从test_login拿到手机登录码后进行登录，获取token
    def test_codelogin(self):
        logdata.info("\n======进入codelogin，获取token=====")
        datajson = json.dumps({"phone": phone, "code": code, "equipmentId": "022781"})
        # 登录接口获取tokenid
        test_login_url = (url + "/openapi/usersystem/user/codelogin")
        r = requests.post(test_login_url, headers=headerJson, data=datajson)
        # 断言
        assert r.json()["msg"] == "操作成功"
        # 拼接时吧字段装换成字符串再进行拼接
        # print("codelogin接口返回值：" + "\n"+json.dumps(r.json(), ensure_ascii=False))

        # 返回值先使用dumps装换成str,再用loads装换成字典，字典在后面能根据valus取key的值
        json_dict = json.loads((json.dumps(r.json(), ensure_ascii=False)))
        # token= json_dict.get('token')
        # 使用jsonpath获取第二层的token值,获取到的是一个列表,使用''.join()把列表转换成str
        token = ''.join(jsonpath.jsonpath(json_dict, '$..data..token'))
        logdata.info("获取的token值：" + "\n" + (''.join(token)))
        # userid =''.join(jsonpath.jsonpath(json_dict,'$..data..userId'))
        # print("获取的token值："+"\n"+(type(userid))
        # print(userid)
        # print(type(''.join(token)))
        # 第二种获取多第二层字典的值的方法，下面是获取userId
        logdata.info("userId:" + (json_dict.get('data')).get('userId'))
        userid = (json_dict.get('data')).get('userId')
        # 把接口中获取的token写入global全局参数的YAML文件，给后续接口使用
        getYaml.repair_data("token", token)
        getYaml.repair_data("userid", userid)
        logdata.info("\n======codelogin接口结束=====")

# if __name__=='__main__':
#     import os
# os.system("locust -f locust_Arknovv_codelogin.py -P 8300 --headless -u 1 -r 1 -t 3")
