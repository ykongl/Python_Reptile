
# json模块
# 用于json与python数据之间的相互转换

import json

# 1.json字符串转换为python数据
json_str = '''[{"provinceName":"美国","currentConfirmedCount":1179041,"confirmedCount":1643499},
{"provinceName":"英国","currentConfirmedCount":222227,"confirmedCount":259559}]'''

# 1.2 把json字符串，转换为Pathon数据

rs = json.loads(json_str)
# print(rs,type(rs)) #list
# print(rs,type(rs[0])) #dict

# 2.把json格式文件，转换为python类型数据
# 2.1构建指向该文件的文件对象
with open('test.json',encoding='utf8') as fp:
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    print(type(python_list[0]))

# 2.2加载该文件对象，转换为python类型数据
