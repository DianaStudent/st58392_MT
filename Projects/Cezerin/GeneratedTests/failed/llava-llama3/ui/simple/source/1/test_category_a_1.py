from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000')

    def tearDown(self):
        self.driver.quit()

    def test_login_page(self):
        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            '//*[contains(@class,"header")]')
        self.assertTrue(header.is_displayed())

        button = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            '//*[contains(@class,"button")]')
        self.assertTrue(button.is_displayed())

        link = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            '//*[contains(@class,"link")]')
        self.assertTrue(link.is_displayed())

        email_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            '//*[contains(@id,"email")]')
        password_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            '//*[contains(@id,"password")]')

        remember_checkbox = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            '//*[contains(@class,"checkbox")]')
        self.assertTrue(remember_checkbox.is_displayed())

if __name__ == '__main__':
    unittest.main()
```