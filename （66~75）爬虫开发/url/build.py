import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/63.0.3239.132 Safari/537.36',
}

# 构建请求对象
request = urllib.request.Request(url = url, headers = headers)

# 发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())