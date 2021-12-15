# 1.导入yaml文件
# 2.使用 with open 形式,确定读取文件的位置
# 4.使用yaml模块中的load方法.读取数据即可

import yaml

# with open("./data.yaml", "r") as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(data)
#     for i in data.values():
#         print(type(i))


with open("./data.yaml", "r", encoding="utf-8") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
