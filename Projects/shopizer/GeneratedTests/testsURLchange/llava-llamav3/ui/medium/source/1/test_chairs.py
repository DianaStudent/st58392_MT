from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time

class TestChairsWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        
    def tearDown(self):
        self.driver.quit()

    def test_chairs_search(self):
        self.driver.get("http://localhost/")

        # Check presence of key interface elements
        header = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_tag_name('header')
        )
        inputs = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_elements_by_tag_name('input')
        )

        # Interact with a button and check the UI updates visually
        button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name('button')
        )
        button.click()
        time.sleep(3)
        self.assertEqual(header.get_attribute('href'), 'http://localhost/')

        # Verify that interactive elements do not cause errors in the UI
        form_fields = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_elements_by_tag_name('form')
        )
        for field in form_fields:
            if 'name' in field.get_attribute('name'):
                self.assertEqual(field.get_attribute('value'), '')

if __name__ == '__main__':
    unittest.main()