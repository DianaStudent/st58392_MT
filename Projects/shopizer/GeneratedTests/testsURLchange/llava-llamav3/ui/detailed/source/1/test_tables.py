```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class TestEcomShopper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chromedriver())
        self.driver.implicitly_wait(10, "seconds")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        self.driver.get("http://localhost/")
        assert(self.driver.find_element_by_tag_name('header'))
        assert(self.driver.find_element_by_tag_name('nav'))
        assert(self.driver.find_element_by_tag_name('footer'))

    def test_check_missing_elements(self):
        self.driver.get("http://localhost/category/tables")
        elements = ['input', 'button']
        for element in elements:
            assert(self.driver.find_element_by_css_selector(element))

    def test_interact_with_ui_elements(self):
        self.driver.get("http://localhost/login")
        self.driver.find_element_by_id('username').send_keys('username')
        self.driver.find_element_by_id('password').send_keys('password')
        self.driver.find_element_by_name('login').click()

if __name__ == '__main__':
    unittest.main()
```