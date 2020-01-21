import urllib.request
import urllib.parse
import http.cookiejar

# 真实模拟浏览器，当发送完post请求的时候，将cookie保存到代码中

# 创建一个cookiejar对象
cj = http.cookiejar.CookieJar()

# 通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)

# 根据handler创建一个opener
opener  = urllib.request.build_opener(handler)


post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201976198111'

form_data = {
    'email': '15929878681',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type':	'web_login',
    'password': '2b960345693fe07445525d27dc40df4fffdd02680c8c1da9f2709f3022960f05',
    'rkey':	'c177ee12a58da2b2d83a728d1ecb1c73',
    'f': 'http%3A%2F%2Fwww.renren.com%2F971759485',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

request = urllib.request.Request(url= post_url, headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
response = opener.open(request, data= form_data)


get_url = 'http://www.renren.com/971759485/profile'

request = urllib.request.Request(url = get_url,headers = headers)

response = opener.open(request)

print('start……')

with open('login.html', 'wb') as fp:
    fp.write(response.read())

print('end……')