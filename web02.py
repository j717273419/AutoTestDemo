import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element(By.ID, 'kw').send_keys("ai")
time.sleep(2)
driver.find_element(By.ID, "su").click()
time.sleep(5)
driver.close()