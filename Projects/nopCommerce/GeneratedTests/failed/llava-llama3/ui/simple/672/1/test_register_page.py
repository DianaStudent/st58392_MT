from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WaitForSecondsUntil
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxRegistrationPage(unittest.TestCase):
    def setUp(self):
        # Set up the driver and navigate to the register page.
        self.driver = Chrome(ChromeDriverManager().get_chrome_driver())
        self.driver.get('http://max/register?returnUrl=%2F')
        WebDriverWait(self.driver, 20).until(self.wait_for_elements_to_load(['header']))

    def tearDown(self):
        # Clean up the driver after each test.
        self.driver.quit()

    def test_register_page(self):
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        self.assertEqual('max', self.driver.title)
        self.assertTrue(self.wait_for_elements_to_load(['header']))
        self.assertTrue(self.wait_for_elements_to_load(['register-title']))

        # Check that these elements exist and are visible.
        self.assertTrue(self.wait_for_elements_to_load(['first-name-field')))
        self.assertTrue(self.wait_for_elements_to_load(['last-name-field'])))

def wait_for_elements_to_load(selector):
    return WebDriverWait(self.driver, 20).until(
```