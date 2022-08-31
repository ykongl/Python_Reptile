
import re
# 1.在不使用 r原串 的时候，遇到转移符如何做


rs = re.findall('a\nbc','a\nbc')
print(rs)


rs = re.findall('a\\nbc','a\\nbc')
print(rs)


rs = re.findall('a\\\nbc','a\\nbc')
print(rs)


rs = re.findall('a\\\\nbc','a\\nbc')
print(rs)


# r原串在正则中就可以消除转移符带来的影响
rs = re.findall(r'a\\nbc', 'a\\nbc')
print(rs)

rs = re.findall(r'a\nbc', 'a\nbc')
print(rs)

# 扩展：可以解决写正则的时候，不符合PEP8规范的问题
rs = re.findall(r'\d', 'a123')
print(rs)
