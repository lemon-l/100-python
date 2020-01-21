from selenium import webdriver 
import time

browser = webdriver.Firefox()
url = 'http://sc.chinaz.com/tupian/shangwurenwutupian.html'

browser.get(url)
time.sleep(3)
with open(r'G:\自动化\picture1.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)

js = 'document.body.scrollTop=1000'
browser.execute_script(js)
time.sleep(3)
with open(r'G:\自动化\picture2.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)


browser.quit()