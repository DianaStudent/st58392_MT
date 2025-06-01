from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_product_filter(self):
        driver = self.driver

        # Wait to ensure page is loaded
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "products")))

        # Confirm initial number of products
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".products .column"))

        # Apply "Brand A" filter
        brand_a_checkbox = driver.find_element(By.CSS_SELECTOR, ".attribute-title + label input")
        brand_a_checkbox.click()
        
        # Wait for UI to update
        time.sleep(2)

        # Verify product count changes
        filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".products .column"))
        if initial_product_count == filtered_product_count:
            self.fail("Product count did not change after applying Brand A filter")

        # Uncheck "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count is restored
        restored_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".products .column"))
        self.assertEqual(initial_product_count, restored_product_count, "Product count not restored after removing Brand A filter")

        # Locate and move price slider
        price_slider = driver.find_element(By.CSS_SELECTOR, ".price-filter .columns.is-mobile .column.has-text-left")
        if not price_slider:
            self.fail("Price slider not found")

        # Use ActionChains to interact with the slider
        action = ActionChains(driver)
        action.click_and_hold(price_slider).move_by_offset(20, 0).release().perform()

        time.sleep(2)

        # Verify product count changes with price filter
        price_filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".products .column"))
        if restored_product_count == price_filtered_product_count:
            self.fail("Product count did not change after applying price filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()