from selenium import webdriver
from time import sleep
import os

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms2.html'
        self.driver.get(file_path)
    def test_checkbox(self):
        swimming = self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()
        sleep(3)
        reading = self.driver.find_element_by_name('reading')
        if not reading.is_selected():
            reading.click()
        sleep(5)
        self.driver.quit()
    def test_radio(self):
        radios = self.driver.find_elements_by_name('gender')
        sleep(2)
        radios[0].click()
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()
