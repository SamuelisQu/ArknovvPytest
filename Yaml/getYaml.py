import yaml
import os

# 获取当前文件的所在目录
file_path = os.path.dirname(__file__) + '/global.yaml'


# 读取所有yaml值

def openyaml():
    # print(file_path)
    with open(file_path, encoding='utf-8') as file1:
        data = yaml.load(file1, Loader=yaml.FullLoader)  # 读取yaml文件
        # data = yaml.dump(file1, sort_keys=True)
    return data


# 读取特定key
def getYamlValue(key):
    with open(file_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    value = data[key]
    return value


# 清空yaml再写入值
def setYaml():
    value = {'name': 'quweiz'}
    with open(file_path, 'w') as f:
        data = yaml.load(value, f)
        print(data)


# 更新、追加操作
def repair_data(key, data):
    with open(file_path, encoding='utf-8') as f:
        dict_temp = yaml.load(f, Loader=yaml.FullLoader)
        try:
            dict_temp[key] = data
        except:
            if not dict_temp:
                dict_temp = {}
            dict_temp.update({key: data})
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(dict_temp, f, allow_unicode=True)


if __name__ == '__main__':
    # print(os.path.abspath(__file__))
    # print(os.path.dirname(__file__))
    # D:\work\PyDjango\locustTest\YAML\global.yaml
    # print(setYaml())
    # print(repair_data('token','1tokenquweizheng'))
    print(getYamlValue('URL'))
    # print(openyaml())
