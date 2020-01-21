import urllib.parse
import urllib.request
import re
import os


def handle_request(url, page):
    url = url + str(page) + '/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)
    return request


def download_image(content):
    pattern = re.compile(
        r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', re.S)
    lt = pattern.findall(content)
    # 遍历列表，依次下载图片
    for image_src in lt:
        # 先处理image_src
        image_src = 'https:' + image_src
        # 发送请求，下载图片
        # 创建文件夹
        dirname = 'picture'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        # 图片名称
        filename = image_src.split('/')[-1]
        filepath = dirname + '/' + filename

        print('%s开始下载····' % filename)
        urllib.request.urlretrieve(image_src, filepath)
        print('%s下载结束' % filename)


def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('起始页码：'))
    end_page = int(input('结束页码：'))

    for page in range(start_page, end_page + 1):
        print('第%s页开始下载····' % page)
        # 生成请求对象
        request = handle_request(url, page)

        # 发送请求对象，获取响应内容
        content = urllib.request.urlopen(request).read().decode()

        # 解析内容，提取所有的图片链接，进行下载
        download_image(content)
        print('第%s下载结束' % page)


if __name__ == '__main__':
    main()
