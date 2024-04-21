import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 判断百度的首页中搜索按钮包含“百度一下”文字
def test():

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    time.sleep(6)
    tes = driver.find_element(By.ID, "su").get_attribute('value')
    time.sleep(2)
    print(tes)
    assert tes == '百度一下'
    driver.close()
