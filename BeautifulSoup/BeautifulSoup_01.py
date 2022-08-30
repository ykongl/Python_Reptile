
# BeautifulSoup对象：代表解析整个文档树
# 支持遍历文档树和搜索文档树中描述的大部分的方法

# 1.导入模块
from bs4 import BeautifulSoup

# 2.创建BeautifulSoup对象
soup = BeautifulSoup('<html>123</html>','lxml')
# 自动补全代码
print(soup)

# find(self,name = ,sttrs = {},recursive = True,text = None,**kwargs)
# name:标签名
# attrs:属性字典
# recursive:是否递归循环查找
# text:根据文本内容查找
# 返回：查找到的第一个元素对象
soup1 = BeautifulSoup('<html><title>123</title><p id= "lei">雷电将军</p><a href = "https://www.baidu.com">百度</a></html>','lxml')

# 根据name查找
print(soup1.find('p'))
print(soup1.find('a'))
# 返回所有的标签
print(soup1.findAll)

# 2.根据属性查找
# 通过命名进行指定
print(soup1.find(id='lei'))

# 使用attrs来指定属性字典，进行查找
print(soup1.find(attrs={'id':'lei'}))


# 3.根据文本text查找
print(soup1.find(text='123'))


# Tag对象
# 对应于原始文档中的xml或html标签
# 属性
# name:获取标签名称
# attrs:获取标签所有的属性的键和值
# text:获取标签的文本字符串
a = soup1.find('a')
print('name = ',a.name)
print('属性 = ',a.attrs)
print('文本 = ',a.text)