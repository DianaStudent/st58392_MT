```
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from html_data import login_page

def setUp(self):
    driver = ChromeDriverManager().get_chrome_driver()
    self.driver = driver
    self.assertTrue("Shopify" in login_page)

def tearDown(self):
    self.driver.quit()

class LoginTest(unittest.TestCase):
    def test_login_process(self):
        self.assertTrue("Shopify" in self.login_page)
        self.assertEqual("Log in", self.login_form.get_by_index(1).text)
        self.assertEqual("Forgot Password", self.login_form.get_by_index(2).text)
        email_field = self.login_form.find_element_by_name("email")
        password_field = self.login_form.find_element_by_name("password")

def test_register_process(self):
    self.assertTrue("Shopify" in self.register_page)
    self.assertEqual("Agree to terms of service", self.register_form.get_by_index(5).text)
    email_field = self.register_form.find_element_by_name("email")
    password_field = self.register_form.find_element_by_name("password")
    phone_field = self.register_form.find_element_by_name("phone")

if __name__ == '__main__':
    unittest.main()
```