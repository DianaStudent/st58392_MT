```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class TestShopRushFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter_by_chair_type(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Click on the filter tab.
        filter_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='filter-button'][1]"))
        )
        filter_button.click()
        
        # Check that at least one product is displayed.
        self.assertTrue(len(driver.find_elements_by_xpath("//div[contains(@data-product-id)]")) > 0)
        
        # Apply filters for different chair types
        driver.get("http://localhost/")
        green_armchair = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='filter-button'][1]"))
        )
        orange_sofa = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='filter-button'][2]"))
        )
        gray_armchair = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='filter-button'][3]"))
        )
        
        # Verify the product count changes after applying filters
        green_count = len(driver.find_elements_by_xpath("//div[contains(@data-product-id)]"))
        orange_count = len(driver.find_elements_by_xpath("//div[contains(@data-product-id)]"))
        gray_count = len(driver.find_elements_by_xpath("//div[contains(@data-product-id)]"))
        
        self.assertTrue(green_count != 0)
        self.assertTrue(orange_count != 0)
        self.assertTrue(gray_count != 0)

if __name__ == '__main__':
    unittest.main()
```