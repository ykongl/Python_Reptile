
# requests基本使用
# 导入模块
import requests

# 2.发送请求，获取响应
response = requests.get('https://www.baidu.com')

# print(response)
# 3.获取响应数据
# ISO-8859-1
# print(response.encoding)
# response.encoding = 'utf-8'
# print(response.text)

# 二进制数据
# print(response.content)
# 解码
# print(response.content.decode(encoding='gbk'))
print(response.content.decode())


# 疫情首页
url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

response2 = requests.get(url)

print(response2.content.decode())