from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 下载 chromedriver(看版本) 放到 D:\Python\Tools\scripts 
# pip install selenium
diver = webdriver.Chrome()


diver.get("http://192.168.232.130:7001")
time.sleep(3)
diver.find_element(by=By.ID,value="username").clear()
time.sleep(1)
diver.find_element(by=By.ID,value="username").send_keys("test")
time.sleep(1)
diver.find_element(by=By.XPATH,value="//*[@id='root']/div/div/section/div/form/div[3]/div/div/div/div/div/div[1]/button").click()

time.sleep(5)
### 测试