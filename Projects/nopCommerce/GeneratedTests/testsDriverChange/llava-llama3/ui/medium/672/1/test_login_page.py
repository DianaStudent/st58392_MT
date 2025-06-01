```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_context import ActionContext
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import KeyDownAction

class TestWooCommerceLoginScenario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_wooocommerce_login_scenario(self):
        # Go to login page
        self.login_page_url = 'http://max/login?returnUrl=%2F'
        self.driver.get(self.login_page_url)
        self.assertTrue(self.driver.current_url == self.login_page_url)

        # Confirm presence of key UI elements: navigation links, inputs, buttons, banners
        self.assertTrue('nav' in self.driver.page_source)
        for nav_link in ['login', 'register']:
            nav_link = self.driver.find_element_by_css_selector(f'nav > a[role*="{Link}"]')
            nav_link_name = nav_link.text_content.strip()
            if nav_link_name == 'Sign In':
                break
            else:
                self.assertFalse(nav_link_name != 'Register')

        for input_type in ['text', 'email']:
            self.assertTrue(self.driver.find_element_by_css_selector(f'form > input[type*="{input_type}"]'))
        for button_type in ['submit', 'button']:
            self.assertTrue(self.driver.find_element_by_css_selector(f'form > button[type*="{button_type}"]'))

        # Interact with elements
        self.driver.find_element_by_css_selector('form > input[name*="username"]').send_keys('max')
        self.driver.find_element_by_css_selector('form > input[name*="password"]').send_keys('123456')

        # Verify that interactive elements do not cause errors in the UI
        self.assertTrue(self.driver.current_url == 'http://max/login?returnUrl=%2F')
```