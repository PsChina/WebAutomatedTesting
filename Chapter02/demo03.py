from selenium import webdriver
from time import sleep

class TestCase:
    def __init__(self):
        try:
            try:
                self.dirver = webdriver.Chrome()
                self.dirver.get('http://wwww.baidu.com')
                self.dirver.maximize_window()
            finally:
                print('init done')
        except:
            print('error')
    def test_prop(self):
        print(self.dirver.page_source)
        print(self.dirver.name)
        print(self.dirver.current_url)
        print(self.dirver.title)
        print(self.dirver.current_window_handle)
        print(self.dirver.window_handles)
        sleep(1)
        print('test_prop done')
    def test_method(self):
        self.dirver.find_element_by_id('kw').send_keys('掘金')
        self.dirver.find_element_by_id('su').click()
        sleep(2)
        self.dirver.back()
        sleep(2)
        self.dirver.refresh()
        sleep(2)
        self.dirver.forward()
        sleep(2)
        self.dirver.close()
        sleep(2)
    def quit(self):
        self.dirver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    case.test_method()
    case.quit()

