from selenium import webdriver 
import time

browser = webdriver.Firefox()
url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='

browser.get(url)
time.sleep(3)
browser.save_screenshot(r'G:\自动化\douban1.png')

# 让browser执行简单的js代码，模拟滚动条滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)
browser.save_screenshot(r'G:\自动化\douban2.png')

# 获取网页的代码，保存到文件中
html = browser.page_source
with open(r'G:\自动化\douban.html', 'w', encoding='utf8') as fp:
    fp.write(html)

browser.quit()