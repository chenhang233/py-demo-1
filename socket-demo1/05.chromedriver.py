from selenium import webdriver
import time
# 下载 chromedriver(看版本) 放到 D:\Python\Tools\scripts 
# pip install selenium
diver = webdriver.Chrome()


diver.get("https://www.npmjs.com/")

time.sleep(5)
