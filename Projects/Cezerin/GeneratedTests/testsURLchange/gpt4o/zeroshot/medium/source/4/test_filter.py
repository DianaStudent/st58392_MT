from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def find_element(self, by, value):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except:
            self.fail(f"Element by {by} with value '{value}' not found.")

    def test_apply_product_filter(self):
        driver = self.driver

        # Locate Brand A checkbox filter and click it
        brand_a_checkbox = self.find_element(By.XPATH, "//label[input[@type='checkbox']][contains(text(), 'Brand A')]")
        brand_a_checkbox.click()

        # Wait for UI to update
        time.sleep(2)

        # Verify that the number of products changes (2 -> 1)
        products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        if not products:
            self.fail("No products found after applying filter.")
        self.assertEqual(len(products), 1)

        # Uncheck the Brand A filter
        brand_a_checkbox.click()
        
        # Wait for UI to update
        time.sleep(2)
        
        # Verify that the number of products restores (1 -> 2)
        products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        if not products:
            self.fail("No products found after removing filter.")
        self.assertEqual(len(products), 2)

        # Locate the price slider and move it
        slider = self.find_element(By.CSS_SELECTOR, ".price-filter .price-filter-values")
        ActionChains(driver).drag_and_drop_by_offset(slider, -50, 0).perform()
        
        # Wait for UI to update
        time.sleep(2)

        # Verify that the product count changes
        products_after_slider = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
        if not products_after_slider:
            self.fail("No products found after applying price filter.")
        self.assertNotEqual(len(products), len(products_after_slider))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()