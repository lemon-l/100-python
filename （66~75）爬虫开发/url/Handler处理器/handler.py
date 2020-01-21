'''
opener 和 urlopen的用法是一模一样的，但是拥有更高级的功能
'''

import urllib.request
import urllib.parse

url = 'http://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

# 创建一个handler
handler = urllib.request.HTTPHandler()

# 通过handler创建一个opener
# opener就是一个对象，一会发送请求的时候，直接使用opener里面的方法即可，不要使用urlopen
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url, headers=headers)

# 发送请求
response = opener.open(request)

print(response.read().decode())