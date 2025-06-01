import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_filters(self):
        # Navigate to a product category
        self.driver.find_element(By.LINK_TEXT, "Home accessories").click()

        # Wait for the filter sidebar to be present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "filter-sidebar")))

        # Select the 'Medium' filter using label-based selection
        medium_filter = self.driver.find_element(By.XPATH, "//label[@data-name='medium']")
        medium_filter.click()

        # Wait for the page to update and verify that the number of visible product items is reduced
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))
        original_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))
        time.sleep(2)  # wait for filter to apply

        new_product_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))
        self.assertLess(new_product_count, original_product_count)

        # Clear all filters
        clear_all_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "clear-all-button")))
        clear_all_button.click()

        # Verify that the number of products returns to the original count
        time.sleep(2)  # wait for filter to remove
        new_product_count_after_clearing = len(self.driver.find_elements(By.CSS_SELECTOR, ".product-item"))
        self.assertEqual(new_product_count_after_clearing, original_product_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()