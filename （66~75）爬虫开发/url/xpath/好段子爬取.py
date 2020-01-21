'''
lt = [{'name': '巴啦啦\n小魔仙'}]

with open('lala.txt', 'w', encoding='utf8') as fp:
    fp.write(str(lt))
'''


fp = open('（66~75）爬虫开发/url/xpath/lala.txt', 'r', encoding='utf8')
string = fp.read()
fp.close()

lt = eval(string)
print(lt[0]['name'])