import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestFilterProducts(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_apply_and_remove_filter(self):
        driver = self.driver
        
        # Wait for the "Brand A" checkbox to be clickable and click it
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute']/label[input[@type='checkbox']][contains(., 'Brand A')]/input"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Check number of visible products after applying "Brand A" filter
        products_after_brand_a_filter = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products_after_brand_a_filter), 1, "The number of products should be 1 after applying Brand A filter.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Check number of visible products after removing "Brand A" filter
        products_after_removing_filter = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        self.assertEqual(len(products_after_removing_filter), 2, "The number of products should be 2 after removing the filter.")

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()