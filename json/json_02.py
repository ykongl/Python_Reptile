
import json
# python数据转为json字符串

# 1.1python类型的数据
json_str = '''[{"provinceName":"美国","currentConfirmedCount":1179041,"confirmedCount":1643499},
{"provinceName":"英国","currentConfirmedCount":222227,"confirmedCount":259559}]'''

rs = json.loads(json_str)

# 1.2把python转换为Json字符串
json_str = json.dumps(rs, ensure_ascii=False)
print(json_str)

# 2.把python以json格式存储到文件中

# 2.1构建要写入文件对象
with open('test.json', 'w', encoding='utf8') as fp:
    json.dump(rs, fp, ensure_ascii=False)
