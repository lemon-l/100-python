import re

string = '我的身高为185厘米，哈哈哈哈哈哈，简直不要太高了'

def fn(a):
    number = int(a.group())
    return str(number - 10)

pattern = re.compile(r'\d+')

ret = pattern.sub(fn, string)

print(ret)