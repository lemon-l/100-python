from selenium import webdriver
import time

#模拟创建一个浏览器对象，然后通过对象去操作浏览器
path = r'F:\软件包\chromedriver\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path= path)

# 让谷歌浏览器打开百度
url = 'http://www.baidu.com/'
browser.get(url)

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往搜索框里面写文字
my_input.send_keys('吴亦凡')
time.sleep(3)
# 查找搜索按钮
button = browser.find_elements_by_class_name('s_btn')[0]
button.click()

time.sleep(3)
which = browser.find_element_by_tag_name('h3')[0]
which.click()

time.sleep(3)

# 关闭浏览器，退出浏览器
browser.quit()