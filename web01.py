import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 使用selenium打开网站，输入关键词，并触发搜索

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
# 填写关键词
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys('数学')
# 触发搜索单击事件
driver.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(3)
driver.close()