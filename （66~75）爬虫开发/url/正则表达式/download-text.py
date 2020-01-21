import urllib.parse
import urllib.request
import re

def handle_request(url, page=None):
    # 拼接指定的url
    if page != None:
        url = url + str(page) + '.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
    } 
    request = urllib.request.Request(url, headers=headers)
    return request


def get_text(a_href):
    # 调用函数构建请求对象
    request = handle_request(a_href)
    # 发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode()
    # 解析内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    lt = pattern.findall(content)
    text = lt[0]
    # 写个正则表达式，匹配图片地址
    pat = re.compile(r'<img .*?>')
    text = pat.sub('', text)
    return text

def parse_content(content):
    pattern = re.compile(r'<a href="(/lizhi/qianming/\d+\.html)"><b>(.*?)</b></a>')
    lt = pattern.findall(content)
    # 返回的lt是一个列表，列表中的元素都是元组，元祖中的第一个元素就是要获取内容的网址，第二个元素就是标题
    for href_title in lt:
        # 获取内容链接
        a_href = 'http://www.yikexun.cn' + href_title[0]
        # 获取内容标题
        title = href_title[-1]
        # 向a_href发送请求，获取响应内容
        text = get_text(a_href)
        # 写入到HTML文件中
        name = 'lizhi.html'
        string = '<h1>%s</h1>%s' %(title, text)
        with open(name, 'a', encoding='utf8') as fp:
                fp.write(string)  

def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input('起始页码：'))
    end_page = int(input('结束页码：'))
    for page in range(start_page, end_page + 1):
        # 根据url和page生成指定的request
        request = handle_request(url, page)
        # print('第%s页开始下载····' % page)
        # 发送请求
        content = urllib.request.urlopen(request).read().decode()
        # 解析文章内容
        parse_content(content)
        # print('第%s下载结束' % page)


if __name__ == '__main__':
    main()
