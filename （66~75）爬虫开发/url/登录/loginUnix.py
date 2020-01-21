import urllib.request
import urllib.parse

'''
1. 前面讲的登录过程：直接抓包找到post地址，发送过去即可登录成功
2. 现在的登录过程：直接抓包发送post不行，因为表单中有一些数据需要从网页中获取到，
    比如formhash。那么，现在的登录过程变成了先发送get请求到登录页面，ran沟通过
    xpath、bs获取需要的表单令牌，然后再发送post请求，开始登录
'''

url = 'http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

formdata = {
    'username': 'Normally',
    'password': 'jsjl246jsjl%3F',
    '_token': 't4rQBaWsUb8ERZxMgV0unAyssw5gMhoDNbL6MD3L',
    '_t': '1573564546352'
}

formdata = urllib.parse.urlencode(formdata).encode()
request = urllib.request.Request(url = url, headers= headers)
response = urllib.request.urlopen(request, data = formdata)

print(response.read().decode('gbk'))