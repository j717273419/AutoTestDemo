import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 选择日期
driver = webdriver.Chrome()
driver.get("https://element-plus.org/zh-CN/component/date-picker.html")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/input').send_keys("2022-07-30")
time.sleep(5)
driver.close()