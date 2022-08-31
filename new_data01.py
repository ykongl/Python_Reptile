
# 提取最新的各国疫情数据

# 1.导入相关模块
import requests
from bs4 import BeautifulSoup
# 2.发送请求，获取疫情首页内容
url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
response = requests.get(url)
home_page = response.content.decode()
# print(home_page)

# 3.使用BeautifulSoup提取疫情数据
soup = BeautifulSoup(home_page,'lxml')
script = soup.find(attrs={'id':'getListByCountryTypeService2true'})
print(script.text)

