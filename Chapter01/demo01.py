from selenium import webdriver
from time import sleep

dirver = webdriver.Chrome()


class TestCase(object):
    def __init__(self):
        self.dirver = webdriver.Chrome()
    def test(self):
        self.dirver.get('http://www.baidu.com')
        self.dirver.find_element_by_id('kw').send_keys('hello')
        self.dirver.find_element_by_id('su').click()
        sleep(4)
        dirver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test()