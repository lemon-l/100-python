import urllib.request
import urllib.parse
from lxml import etree
import time
import os


def handle_request(url, page):
    # 由于第一页和后面的规律不一样，所以需要进行判断
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/72.0.3626.96 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def download_image(image_src):
    dirpath = 'sex'
    # 创建一个文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    
    # 搞个文件名
    filename = os.path.basename(image_src)
    # 搞图片路径
    filepath = os.path.join(dirpath, filename)
    # 发送请求，保存图片
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/72.0.3626.96 Safari/537.36'
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


# 解析内容，并下载图片
def parse_content(content):
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # 懒加载：用到的时候再进行加载
    # print(image_list)
    # print(len(image_list))
    # 遍历列表，依次下载图片
    for image_src in image_list:
        download_image(image_src)


def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'
    # http://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        time.sleep(1)


if __name__ == '__main__':
    main()
