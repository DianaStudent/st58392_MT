from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver

        # Wait for the filter sidebar to appear
        try:
            filter_sidebar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar not found: {e}")

        # Find and select the filter checkbox "Composition: Matt paper"
        try:
            composition_filter = driver.find_element(By.XPATH, "//label/span[contains(text(), 'Matt paper')]/..")
            initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))

            composition_filter.click()

            # Wait until the product count changes
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".js-product")) != initial_product_count
            )

            filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
            self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")

        except Exception as e:
            self.fail(f"Filter application failed: {e}")

        # Remove the filter to verify it changes back
        try:
            composition_filter.click()

            # Wait until product count reverts
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".js-product")) == initial_product_count
            )
            
            reverted_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
            self.assertEqual(initial_product_count, reverted_product_count, "Product count did not revert after removing filter")

        except Exception as e:
            self.fail(f"Filter removal failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()