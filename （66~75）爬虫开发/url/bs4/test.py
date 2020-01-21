from bs4 import BeautifulSoup
# 生成对象
soup = BeautifulSoup(open('（66~75）爬虫开发/url/bs4/soup_text.html', encoding='utf8'), 'lxml')

print(soup.select('#feng')[0]['href'])