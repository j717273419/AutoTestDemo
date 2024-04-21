import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# # 弹框提示-普通弹窗，只有一个alert
# driver = webdriver.Chrome()
# driver.get("https://sahitest.com/demo/alertTest.htm")
# # 触发单击事件
# driver.find_element(By.NAME, "b1").click()
# time.sleep(3)
# # 点击弹窗的确认按钮
# driver.switch_to.alert.accept()
# time.sleep(5)
# driver.close()

# # 弹框提示-确认弹窗，有确认和取消
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://sahitest.com/demo/confirmTest.htm")
# # 触发单击事件
# driver.find_element(By.NAME, "b1").click()
# time.sleep(3)
# # 点击弹窗的确认按钮
# driver.switch_to.alert.accept()
# time.sleep(3)
# # 触发单击事件
# driver.find_element(By.NAME, "b1").click()
# # 点击弹窗的取消按钮
# driver.switch_to.alert.dismiss()
# time.sleep(5)
# driver.close()

# 弹框提示-输入确认弹窗，有确认和取消，还有输入框
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/promptTest.htm")
# 触发单击事件
driver.find_element(By.NAME, "b1").click()
time.sleep(3)
driver.switch_to.alert.send_keys('test')
time.sleep(3)
# 点击弹窗的确认按钮
driver.switch_to.alert.accept()
time.sleep(3)
# # 触发单击事件
# driver.find_element(By.NAME, "b1").click()
# time.sleep(3)
# driver.switch_to.alert.send_keys('test2')
# time.sleep(3)
# # 点击弹窗的取消按钮
# driver.switch_to.alert.dismiss()
# print(driver.switch_to.alert.text)
# time.sleep(5)
driver.close()
