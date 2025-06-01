from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from time import sleep

class TestShopsterLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost/')

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        account_icon = self.driver.find_element_by_css_selector('a[title="Account"]')
        account_icon.click()
        login_link = self.driver.find_element_by_css_selector('a[title="Login"]')
        login_link.click()
        
        email_field = self.driver.find_element_by_name('email')
        password_field = self.driver.find_element_by_name('password')
        email_field.send_keys('test2@user.com')
        password_field.send_keys('test**11')
        
        login_button = self.driver.find_element_by_name('login')
        login_button.click()
        
        WebDriverWait(self.driver, 20).until(lambda x: 'http://localhost/my-account' in x.current_url())
        break
```