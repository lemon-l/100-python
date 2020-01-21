import re 

'''
string = '<p><div><span>猪八戒</span></div></p>'

pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')

ret = pattern.search(string)

print(ret)
'''

'''
# 非贪婪

string = '<div>猪八戒</div></div></div>'

pattern = re.compile(r'<div>.*?</div>')

ret = pattern.search(string)

print(ret)
'''

# # 单行、多行匹配
# string = ''' give you some punlish
# love you like you love all  the world
# love you very much
# hhhh'''

# string1 = '''<div> 茅屋为秋风所破歌
# 八月秋高风怒号
# 卷我无上三层毛
# 茅飞渡江洒江郊
# 高者挂罥长林梢
# 低着抛转陈堂奥
# </div>
# '''

# pattern1 = re.compile(r'<div>(.*?)</div>', re.S)
# pattern = re.compile(r'^love', re.M)

# ret = pattern.findall(string)
# ret1 = pattern1.findall(string1)

# print(ret1)
# print(ret)


string = 'i love you, you love him, ye'

pattern = re.compile(r'love')

# ret = pattern.sub('hate', string)
ret = re.sub(r'love', 'hate', string)

print(ret)