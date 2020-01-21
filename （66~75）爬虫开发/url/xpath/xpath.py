from lxml import etree

# 生成对象
tree = etree.parse('（66~75）爬虫开发/url/xpath/xpath.html')

# ret = tree.xpath('//div[@class="tang"]/ul/li[1]/text()')

# ret = tree.xpath('//div[@class="tang"]/ul/li[last()]/a/@href')

# ret = tree.xpath('//div[@class="tang"]/ul/li[@class="love" and @name="yang"]/text()')

# contains匹配标签
# ret = tree.xpath('//li[contains(@class, "l")]')
# contains匹配内容
# ret = tree.xpath('//li[contains(text(), "爱")]/text()')

# ret = tree.xpath('//li[starts-with(@class, "ba")]/text()')

# ret = tree.xpath('//div[@class="song"]//text()')

ret = tree.xpath('//div[@class="song"]')
string = ret[0].xpath('string(.)')
print(string.replace('\n', '').replace('\t', ''))