from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_product_filter(self):
        driver = self.driver

        try:
            # Wait for products to be loaded
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products"))
            )

            # Check initial number of product cards
            initial_products = driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
            self.assertEqual(len(initial_products), 2, "Initial product count does not match expected value.")

            # Find and click the "Brand A" checkbox
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//label[text()='Brand A']/input"))
            )
            brand_a_checkbox.click()
            time.sleep(2)

            # Check number of product cards after applying "Brand A" filter
            filtered_products = driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
            self.assertEqual(len(filtered_products), 1, "Product count after applying 'Brand A' filter is incorrect.")

            # Uncheck the "Brand A" filter
            brand_a_checkbox.click()
            time.sleep(2)

            # Check number of product cards after removing "Brand A" filter
            final_products = driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
            self.assertEqual(len(final_products), 2, "Product count after removing 'Brand A' filter is incorrect.")

            # Interact with price component to demonstrate changing price filtering
            # Note: Assuming the price slider can be adjusted by clicking or dragging
            price_slider = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-filter .columns.is-gapless"))
            )
            # This will require more advanced actions than simple clicks, so typically would require drag and drop
            ActionChains(driver).drag_and_drop_by_offset(price_slider, 50, 0).perform()
            time.sleep(2)

            adjusted_price_products = driver.find_elements(By.CSS_SELECTOR, ".content.product-caption")
            self.assertEqual(len(adjusted_price_products), 1, "Product count after adjusting price filter is incorrect.")
        
        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()