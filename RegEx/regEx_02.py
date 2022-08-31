
import re
# 1.findall方法，返回匹配的结果列表
rs = re.findall(r'\d+','chuan123zhi34')
print(rs)
# 2.findall方法中，flag参数的作用
rs = re.findall('a.bc','a\nbc',re.DOTALL)
rs = re.findall('a.bc','a\nbc',re.S)
# re.findall(pattern,string,flags=0)
# pattern:正则表达式
# string:从那个字符串中查找
# flags:匹配模式
# 返回String中与pattern匹配的结果列表
print(rs)

# 3.findall方法中分组的使用
rs = re.findall('a(.+)bc','a\nbc',re.DOTALL)
print(rs) # ['\n']