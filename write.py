# 1.导入yaml文件
# 2.准备写入的数据
# 3.使用 with open 形式,确定写入文件的位置
# 4.使用yaml模块中的dump方法.将数据和文件流传入即可

import yaml

data = ['1', '2', {'name': ['xiaoming', 'xiaohong'], 'age': '18'}, [{'name': '小明', 'age': '28'}, '3', '4'], '5',
        ['7', '8']]
with open("./hello.yaml", "w") as f:
    yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
