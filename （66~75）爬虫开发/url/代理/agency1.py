import urllib.request
import urllib.parse

# 创建handler    163.204.242.144:9999
handler = urllib.request.ProxyHandler({'http': '114.215.95.188:3128'})
# 常见opener
opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/s?ie=UTF-8&WD=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

response = opener.open(request)\

with open('ip.html', 'wb') as fp:
    fp.write(response.read())
