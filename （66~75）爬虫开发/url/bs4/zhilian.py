'''
由于智联网的改版，这个暂时爬不了，但是学习学习方法也是挺好的
'''

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import time

class Spider(object):
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
    def __init__(self, jl, kw, start_page, end_page):
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        # 定义一个空列表，定义所有的空信息
        item = []

    # 根据page拼接指定的url，然后生成请求对象
    def handle_request(self, page):
        data = {
            'jl': self.jl,
            'kw': self.kw,
            'p': page,
        }
        url_now = self.url + urllib.parse.urlencode(data)
        # 构建请求对象
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/72.0.3626.96 Safari/537.36'
        }
        request = urllib.request.Request(url_now, headers=headers)
        return request
    
    # 解析内容函数
    def parse_content(self, content):
        # 生成对象
        soup = BeautifulSoup(content, 'lxml')
        # 找到所有的table，一个工作岗位就是一个table，遍历这个table列表，
        # 然后通过table的对象的select、find方法去找每一条记录的具体信息
        table_list = soup.select('#newlist_list_content_table > table')[1:]
        # 遍历这个table_list,依次获取每一个数据
        for table in table_list:
            # 获取职位名称
            zwmc = table.select('.zwmc > div > a')[0].text
            # 获取公司名称
            gsmc = table.select('.gamc > a')[0].text
            # 获取职位月薪
            zwyx = table.select('.zwyx')[0].text
            # 获取工作地点
            gzdd = table.select('.gzdd')[0].text
            # 获取发布时间
            gxsj = table.select('.gxsj > span')[0].text
            # 存放到字典中
            item = {
                '职位名称': zwmc,
                '公司名称': gsmc,
                '职位月薪': zwyx,
                '工作地点': gzdd,
                '发布时间': gxsj,
            }
            # 再存放到列表中
            self.items.append(item)
        
    # 爬取程序
    def run(self):
            # 循环爬取每一页数据
        for page in range(self.start_page, self.end_page + 1):
            request = self.handle_request(page)
            # 发送请求，获取内容
            content = urllib.request.urlopen(request).read().decode()
            # 解析内容
            self.parse_content(content)
            time.sleep(2)
        
        # 将列表数据保存到文件中
        string = json.dumps(self.items)
        with open('zhilian.txt', 'w', encoding='utf8') as fp:
            fp.write(string)


def main():
    jl = input('输入工作地点： ')
    kw = input('输入工作关键字： ')
    start_page = int(input('输入起始页码： '))
    end_page = int(input('输入结束页码'))

    # 创建对象，启动爬取程序
    spider = Spider(jl, kw, start_page, end_page)
    spider.run()


if __name__ == '__main__':
    main()
