'''
豆瓣 —— ajax
'''

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=20&page_start=1'

page = int(input('输入你要的页数：'))
number = 10
data = {
    'start': page,
    'limit': number,
}

query_string  = urllib.parse.urlencode(data)

url += query_string 

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

request = urllib.request.Request(url=url, headers = headers)

response = urllib.request.urlopen(request)

print(response.read().decode())