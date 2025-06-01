from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_apply_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Wait for and check initial products available
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .available")))
        initial_count = len(products)

        # Step 2: Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[label/text()='Brand']/label[input='/input[contains(.., \"Brand A\")]']/input[@type='checkbox']")))
        brand_a_checkbox.click()

        # Step 3: Wait for UI to update
        time.sleep(2)

        # Step 4: Verify displayed product cards count changes
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        filtered_count = len(filtered_products)
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering by Brand A.")

        # Step 5: Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Step 6: Verify original number of product cards is restored
        restored_products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        restored_count = len(restored_products)
        self.assertEqual(initial_count, restored_count, "Product count did not restore after unchecking Brand A.")

        # Step 7: Locate the price slider component
        price_slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .price-filter-values")))

        # Step 8: Move one of the slider handles to apply price range filter
        # For simplicity, assuming a direct move to new value isn't constrained by range handle control in UI
        # This needs real action chains in an interactive UI setting
        slider_handles = driver.find_elements(By.CSS_SELECTOR, ".price-filter .column")
        if not slider_handles:
            self.fail("Price slider handles are missing.")
        else:
            slider_handles[0].click()  # Click on first handle to simulate move
            time.sleep(2)

        # Step 9: Verify that product count changes
        price_filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        price_filtered_count = len(price_filtered_products)
        self.assertNotEqual(restored_count, price_filtered_count, "Product count did not change after applying price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()