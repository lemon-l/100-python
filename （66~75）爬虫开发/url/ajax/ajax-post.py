'''
KFC 
'''
import urllib.request
import urllib.parse

url_post = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

city = input('输入查询的城市： ')
page = int(input('输入查询的页码： '))
num = int(input('一页有多少个： '))
form_data = {
    'cname': city,
    'pid': '',
    'pageIndex': page,
    'pageSize': num,
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

request = urllib.request.Request(url=url_post, headers = headers)

form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request, data= form_data)

print(response.read().decode())