'''
url只能由特定的字符组成，字母、数字、下划线
如果出现其他的，比如$ 空格 中文，就要对其进行编码
'''

import urllib.parse

'''
url = 'https://www.baidu.com/index.html?name=狗蛋&pwd=123456'
ret = urllib.parse.quote(url)  # 编码
re = urllib.parse.unquote(ret) # 解码
print(ret)
print(re)
'''

url = 'http://www.baidu.com/index.html'

# 假如参数有 name age sex height


name = 'lemonl'
age = '18'
sex = 'girl'
height = '158'

data = {
    'name': name,
    'age': age,
    'sex': sex,
    'height': height,
}

query_string = urllib.parse.urlencode(data)
print(query_string)

'''
# 遍历字典
items = []
for i, j in data.items():
    items.append(i + '=' + str(j))
query_string = '&'.join(items)
'''
url = url + '?' + query_string
print(url)
