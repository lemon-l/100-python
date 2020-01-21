from random import randint     
#使用random模块的randint函数生成指定范围的随机数
face = randint(1,20)


import math 
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
area = math.sqrt(a*c*b)      
#使用sqrt函数来计算平方根
char = (a*c*b)**0.5
print('%d a 和 %d b 的差为 %d： ' %(a, b, abs(a-b)))  
#使用python的内置函数 abs() 函数取绝对值来处理负数
print('这两个值分别为 %d and %d' % (area,char))

