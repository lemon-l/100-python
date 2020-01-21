# 在屏幕上显示跑马灯文字
'''
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
'''

# 设置函数产生指定长度的验证码，由大小写字母和数字构成
'''
from random import randint
import random

def get_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_index = len(all_chars)-1
    code = ''
    for i in range(code_len):
        index = randint(0, last_index)
        code += all_chars[index]
    return code

print(get_code())
'''

#获取文件名的后缀名
'''
def get_suffix(filename, has_dot=False):
    """

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

print(get_suffix('test.txt',True))
'''

#当返回多个值时的技巧
'''
#******************python的函数返回多个值其实就是返回一个tuple***************
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

x = [15,10,23,78,1,58,1]
r = max2(x)               #在这里先用一个变量将其存起来，然后再进行输出
print(r)
'''

#打印杨辉三角
'''
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
'''
