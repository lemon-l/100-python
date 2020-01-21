# 计算m!/(n!(m-n)!)
'''
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)
'''

# 重构函数
'''
def factor(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

m = int(input('m = '))
n = int(input('n = '))
print(factor(m)// factor(n)//factor(m-n))
'''
'''
# 回文
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


# 素数
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


# 根据具体情况进行调用
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
'''