
# 提取最新的各国疫情数据

# 1.导入相关模块
import re
import requests
from bs4 import BeautifulSoup
import json

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
# print(json_str)

# 5.把json数据转换为python类型的数据
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)



# 把python转换为Json字符串

files = json.dumps(last_day_corona_virus,ensure_ascii=False)

with open('tt.json','w',encoding='utf8') as fp:
    json.dump(files,fp,ensure_ascii=False)