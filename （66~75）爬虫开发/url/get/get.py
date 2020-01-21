import urllib.request
import urllib.parse

word = input('输入你要查找的内容： ')
url = 'http://www.baidu.com/s?'
data = {
    'ie': 'utf-8',
    'wd': word,
}

query_string = urllib.parse.urlencode(data)
url += query_string

response = urllib.request.urlopen(url)

filename = word + '.html'
with open(filename, 'wb') as fp:
    fp.write(response.read())