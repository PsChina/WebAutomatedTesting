from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
# ID = 'id'
# LINK_TEXT = 'link text'
# NAME = 'name'
# PARTIAL_LINK_TEXT = 'partial link'
# TAG_NAME = 'tag name'
# XPATH = 'xpath'


def get_element(dirver, *loc):
    e = dirver.find_element(*loc)
    return e

if __name__ == '__main__':
    try:
        try:
            dirver = webdriver.Chrome()
            dirver.get('http://baidu.com')
            sleep(1)
            get_element(dirver,By.ID,'kw').send_keys('你好')
            get_element(dirver,By.ID,'su').click()
            sleep(3)
        finally:
            dirver.quit()
    except :
        print('程序异常')