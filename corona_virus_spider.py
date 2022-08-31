# 导包
import requests
import json
from bs4 import BeautifulSoup
import re
from tqdm import tqdm


class CoronaVirusSpider(object):
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'


    # 1.发送请求，获取疫情首页
    def get_content_from_url(self, url):
        """
        根据URL,获取响应内容的字符串数据
        :param url: 请求的URL
        :return: 相应内容的字符串
        """
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self, home_page, tag_id):
        """
        解析首页内容，获取解析后的python数据
        :param home_page: 首页内容
        :return: 解析后的python数据
        """
        # 2.从疫情首页，提取最近一日各国疫情数据
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(attrs={'id': tag_id})
        # print(script.text)
        text = script.text
        # 3.从疫情数据中，获取json格式的字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)

        # 4.把json格式的字符串转换为python类型
        last_day_corona_virus = json.loads(json_str)
        return last_day_corona_virus

    def load(self,path):
        """
        根据路径加载数据
        :param path:
        :return:
        """
        with open(path,encoding='utf8') as fp:
            data = json.load(fp)
        return data
    def save(self, last_day_corona_virus, path):
        # 5.以json格式保存，最近一日各国疫情数据
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(last_day_corona_virus, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 1.获取首页内容
        home_age = self.get_content_from_url(self.home_url)
        # 2.解析数据
        last_day_corona_virus = self.parse_home_page(home_age, tag_id='getListByCountryTypeService2true')
        # 3.保存数据
        self.save(last_day_corona_virus, 'last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集从1月23号以来各国疫情数据
        :return:
        """
        # 1.加载各国疫情数据
        last_day_corona_virus = self.load(path='last_day_corona_virus.json')
        # print(last_day_corona_virus)
        corona_virus = self.parse_corona_virus(last_day_corona_virus)
        # 5.把列表以json格式保存为文件
        self.save(corona_virus, 'corona_virus.json')

    # 国内的疫情数据
    def crawl_list_day_corona_virus_of_china(self):
        """
        采集最近一日各省疫情数据
        :return:
        """
        # 1.发送请求，获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        data = self.parse_home_page(home_page,tag_id='getAreaStat')
        # 3.保存疫情数据
        self.save(data,'crawl_list_day_corona_virus_of_china.json')

    def crawl_corona_virus_of_china(self):
        """
        采集从1月22日以来的全国各省的疫情数据
        :return:
        """
        # 加载最近一日全国疫情信息
        last_day_corona_virus_of_china = self.load(path='crawl_list_day_corona_virus_of_china.json')
        corona_virus = self.parse_corona_virus(last_day_corona_virus_of_china)
        self.save(corona_virus, 'corona_virus_china.json')

    def parse_corona_virus(self, last_day_corona_virus_of_china):
        corona_virus = []
        # 遍历最近一日全国疫情信息，获取全国疫情URL
        for province in tqdm(last_day_corona_virus_of_china, '采集1月22日以来的全国疫情数据'):
            # 3.发送请求，获取各省从1月23号至今的json数据
            statistics_data_url = province['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # print(statistics_data_json_str)
            # 4.把json数据转换为python类型的数据，添加到列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = province['provinceName']
                if province.get('countryShortCode'):
                    one_day['countryShortCode'] = province['countryShortCode']

            # print(statistics_data)
            corona_virus.extend(statistics_data)

            # 5.把列表以json格式保存为文件
        return corona_virus

    def run(self):
        self.crawl_corona_virus_of_china()
        # self.crawl_list_day_corona_virus_of_china()
        # self.crawl_last_day_corona_virus()
        # self.crawl_corona_virus()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()