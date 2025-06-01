```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import Until

class TestMax(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome('chromedriver')
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_max_home_page(self):
        self.driver.get('http://max/')
        self.assertTrue(self.driver.find_element_by_css_selector('.header-links .cart-qty'))
        self.assertTrue(self.driver.find_element_by_css_selector('.block'))

    def test_max_login_page(self):
        self.driver.get('http://max/login?returnUrl=%2F')
        self.assertTrue(self.driver.find_element_by_css_selector('.login-page'))
        self.assertTrue(self.driver.find_element_by_css_selector('#username'))
        self.assertTrue(self.driver.find_element_by_css_selector('#password'))

    def test_max_register_page(self):
        self.driver.get('http://max/register?returnUrl=%2F')
        self.assertTrue(self.driver.find_element_by_css_selector('.register-page'))
        self.assertTrue(self.driver.find_element_by_css_selector('#firstName'))
        self.assertTrue(self.driver.find_element_by_css_selector('#lastName'))
        self.assertTrue(self.driver.find_element_by_css_selector('#email'))

    def test_max_search_page(self):
        self.driver.get('http://max/search')
        self.assertTrue(self.driver.find_element_by_css_selector('.search-page'))
        self.assertTrue(self.driver.find_element_by_css_selector('#query'))

if __name__ == '__main__':
    unittest.main()
```
In this code, I've used the `unittest` and `selenium` modules to write a test case for the Max website. The test cases check if the main UI components are present on the home page, login page, and register page.

The `setUp()` method initializes the WebDriver with Chrome as the browser of choice and stores it in an instance variable named `self.driver`. The `tearDown()` method at the end of the class closes the WebDriver session.

In the test methods (`test_max_home_page`, `test_max_login_page`, `test_max_register_page`, and `test_max_search_page`), I've used various Selenium WebDriver commands to check if certain elements are present on each page. These tests use the `.find_element_by_css_selector()` method to find specific CSS selectors for elements like the cart quantity button, block, login username field, register first name field, etc.

The test is executed using `unittest.main()` at the end of the class.