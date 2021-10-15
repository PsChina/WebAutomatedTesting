from selenium import webdriver
from time import sleep

class TestCase:
    def __init__(self):
        try:
            try:
                self.driver = webdriver.Chrome()
                self.driver.get('http://wwww.baidu.com')
                self.driver.maximize_window()
            finally:
                print('init done')
        except:
            print('error')
    def test_prop(self):
        print(self.driver.page_source)
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        sleep(1)
        print('test_prop done')
    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('掘金')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()
        sleep(2)
        self.driver.close()
        sleep(2)
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    case.test_method()
    case.quit()

