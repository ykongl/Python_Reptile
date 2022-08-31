
# 正则表达式
# 1.导入正则模块
import re

# 字符匹配
rs = re.findall('123','22244451123556')
# .号能匹配\n以外的所有符号
rs = re.findall('a.b','a\nb')
rs = re.findall('a[bc]d','abd')

# 预定义的字符串
# \d匹配[0-9]的数字
rs = re.findall('\d','123')
# \w匹配字母数字_和中文
rs = re.findall('\w','Az123_中文$%')


# 数量词
# *前面的一个匹配模式出现0次或多次
# +前面的一个匹配模式出现1次或多次
# ?前面的一个匹配模式出现0或1次
rs = re.findall(r'a\d*', 'a1234')
rs = re.findall(r'a\d+', 'a')
rs = re.findall(r'a\d?', 'a123')
rs = re.findall(r'a\d{2}', 'a123')
print(rs)
