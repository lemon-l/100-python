'''
post

[注：] 
'''
import urllib.request
import urllib.parse

# 获取url地址
post_url = 'https://fanyi.baidu.com/sug'

word = input('输入你要查询的单词： ')

# 构建post表单数据
form_data = {
    'kw': word,
}

# 发送请求的过程
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
}

# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)

#处理post表单数据
form_data = urllib.parse.urlencode(form_data).encode()

# 发送请求
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode()
