
# 提取最新的各国疫情数据

# 1.导入相关模块
import re

import requests
from bs4 import BeautifulSoup
# 2.发送请求，获取疫情首页内容
url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
response = requests.get(url)
home_page = response.content.decode()
# print(home_page)

# 3.使用BeautifulSoup提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(attrs={'id':'getListByCountryTypeService2true'})
# print(script.text)
text = script.text

# 4.使用正则表达式，提取json字符串
json_str = re.findall(r'\[.+\]', text)[0]
print(json_str)