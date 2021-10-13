from selenium import webdriver
from time import sleep

dirver = webdriver.Chrome()
dirver.get('http://www.baidu.com')
dirver.find_element_by_id('kw').send_keys('hello')
dirver.find_element_by_id('su').click()

sleep(4)

dirver.quit()