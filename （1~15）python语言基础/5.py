# 完美数
'''
for i in range(1, 1001):
        k = 0
        for j in range(1, i):
            if (i % j == 0):
                k += j
        if i == k:
            print(i)
'''
# 百钱百鸡
'''
for num_cock in range(0, 100):
    for num_hen in range(0, 100):
            #这块用了公式，自己可以推出来
        if 14*num_cock + 8*num_hen - 200 == 0 and 100-num_hen-num_cock >= 0:
            print('公鸡{0}只，母鸡{1}只，雏鸡{2}只'.format(
                num_cock, num_hen, (100-num_cock-num_hen)))
'''
# 斐波拉切数列
'''
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
'''
# 判断回文
num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
