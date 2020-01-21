import os
import urllib.parse
import urllib.request

url = 'http://tieba.baidu.com/f?ie=utf-8&'

# 输入吧名，起始页码，结束页码，然后在当前文件夹来创建一个以吧名未名自带的文件夹，
# 里面是每一页的html内容，文件名是吧名_page.html

ba_name = input('输入吧名： ')
start_page = int(input('输入起始页码： '))
end_page = int(input('输入结束页码： '))

# 创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)

# 用循环来爬去每一页的数据
for page in range(start_page, end_page):
    # page就是当前页码，
    # 凭借url的过程
    url = 'http://tieba.baidu.com/f?ie=utf-8&'
    data = {
        'kw': ba_name,
        'pn': (page-1)*50,
    }
    data = urllib.parse.urlencode(data)
    url += data

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)

    print('第%s页开始下载……' % page)
    response = urllib.request.urlopen(request)

    # 生成文件名
    filename = ba_name + '_' + str(page) + '.html'
    # 拼接文件路径
    filepath = ba_name + '/' + filename

    with open(filepath, 'wb') as fp:
        fp.write(response.read())
    print('第%s页结束下载……' % page)
