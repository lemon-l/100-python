'''
两种方式保存图片：
'''

import urllib.request

image_url = 'http://p0.ifengimg.com/pmop/2018/0821/1B135A37B6ABFCFBDE55BCC858B3CDF4169A89D8_size156_w932_h1163.jpeg'

'''
response = urllib.request.urlopen(image_url)

with open('fuji.jpg', 'wb') as fp:
    fp.write(response.read())
'''

urllib.request.urlretrieve(image_url, 'muscle.jpg')