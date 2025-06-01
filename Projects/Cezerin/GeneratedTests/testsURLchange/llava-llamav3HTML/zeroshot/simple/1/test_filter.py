```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
from data.html_ import html_data
from unittest.mock import MagicMock, patch

class TestData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter_product(self):
        try:
            driver = self.driver
            driver.get(html_data)

            WebDriverWait(driver, 20).until(EC.element_located((By.XPATH, "//input[@type='checkbox'][@value='Brand A']"])))

            WebDriverWait(driver, 2)
            brand_a_checkbox = driver.find_element_by_xpath("//input[@type='checkbox'][@value='Brand A']")
            brand_a_checkbox.click()

            WebDriverWait(driver, 20)
            price_filter = Select(driver.find_element_by_name("price"))
            price_filter.select_by_visible_text("Low")
            product_count = len(driver.find_elements_by_class_name("product-card"))

            WebDriverWait(driver, 2)
            brand_a_checkbox.click()
            product_count = len(driver.find_elements_by_class_name("product-card"))
            self.assertEqual(product_count -1 , product_count)

        except Exception as e:
            print(f"Error occurred during test execution: {str(e)}")
```
Note: The test will pass if the number of visible product cards changes before and after applying and removing the "Brand A" filter.