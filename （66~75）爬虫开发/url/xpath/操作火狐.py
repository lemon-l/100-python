from selenium import webdriver 
import time

browser = webdriver.Firefox()
url = 'http://www.baidu.com'
browser.get(url)
time.sleep(3)


# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往搜索框里面写文字
my_input.send_keys('吴亦凡')
time.sleep(3)
# 查找搜索按钮
button = browser.find_elements_by_class_name('s_btn')[0]
button.click()
time.sleep(3)
browser.save_screenshot(r'G:\kris.png')

time.sleep(3)

# 关闭浏览器，退出浏览器
browser.quit()