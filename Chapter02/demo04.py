from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
#http://sahitest.com/demo

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.e = self.driver.find_element_by_id('t1')

    def test_webelement_prop(self):
        
        # e 就是 WebElement
        e = self.e
        print(type(e))
        print(e.id) # 标识
        print(e.tag_name) # tagName 标签名
        print(e.rect) # 宽高和坐标
        print(e.text) # 文本内容
        print(e.size) # 宽高
    
    def test_webelement_method(self):
        e = self.e
        e.send_keys('123')
        sleep(1)
        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        sleep(3)
        e.clear()
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))

        # e1 = self.driver.find_element(By.LINK_TEXT,'Back')
        # e1.click()
        # e2 = self.driver.find_element(By.LINK_TEXT,'Form Test')
        # e2.click()
        
    def test_webelement_method2(self):
        e = self.driver.find_element(By.XPATH,'/html/body/form[1]')
        e.find_element_by_id('t1').send_keys('test_method2')

    def test_window(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        windows = self.driver.window_handles
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)

if __name__ == '__main__':
    case = TestCase()
    #case.test_webelement_prop()
    # case.test_webelement_method()
    # case.test_webelement_method2()
    case.driver.get('http://www.baidu.com')
    case.test_window()
    # case.driver.quit()