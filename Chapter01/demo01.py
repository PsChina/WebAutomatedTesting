from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
    def test(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('hello')
        self.driver.find_element_by_id('su').click()
        sleep(4)
        driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test()