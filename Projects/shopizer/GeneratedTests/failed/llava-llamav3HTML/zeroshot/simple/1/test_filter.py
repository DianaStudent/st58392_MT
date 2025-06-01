from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assertions
from selenium.webdriver.support.ui import Select

class TestProductFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://localhost/"

    def tearDown(self):
        self.driver.quit()

    def test_filter_product(self):
        try:
            # Click on the filter tab
            filter_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@value='filter']")))
            filter_button.click()

            # Check if at least one product is displayed
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'col-lg-3 col-md-6')]")))
        except Exception as e:
            self.fail(str(e))

if __name__ == '__main__':
    unittest.main()
```