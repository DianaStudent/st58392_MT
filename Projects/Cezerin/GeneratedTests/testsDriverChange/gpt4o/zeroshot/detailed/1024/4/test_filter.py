from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_filter_brand_and_price(self):
        # Wait until products and filters are fully loaded
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".content.product-caption")))

        # Initial product count
        initial_products = self.driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
        initial_count = len(initial_products)

        # Locate and apply the "Brand A" checkbox
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='attribute-title' and text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")))
        brand_a_checkbox.click()

        # Confirm it is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox should be selected")

        # Wait 2 seconds and verify that the number of product cards is reduced
        time.sleep(2)
        filtered_products = self.driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
        filtered_count = len(filtered_products)
        self.assertLess(filtered_count, initial_count, "Product count should decrease after applying Brand A filter")

        # Uncheck the filter
        brand_a_checkbox.click()
        self.assertFalse(brand_a_checkbox.is_selected(), "Brand A checkbox should be unselected")

        # Wait 2 seconds and confirm product count is restored
        time.sleep(2)
        restored_products = self.driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
        restored_count = len(restored_products)
        self.assertEqual(restored_count, initial_count, "Product count should restore after unchecking Brand A filter")

        # Locate price slider and adjust maximum price
        right_slider = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".price-filter .ui-slider-handle[aria-valuemax][aria-valuenow]")))
        self.driver.execute_script("arguments[0].setAttribute('style', 'left: 50%;')", right_slider)
        self.driver.execute_script("arguments[0].setAttribute('aria-valuenow', 1159)", right_slider)

        # Wait 2 seconds and verify that the number of product cards is reduced
        time.sleep(2)
        price_filtered_products = self.driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
        price_filtered_count = len(price_filtered_products)
        self.assertLess(price_filtered_count, initial_count, "Product count should decrease after applying price filter")

if __name__ == "__main__":
    unittest.main()