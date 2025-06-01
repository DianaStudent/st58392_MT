import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestProductFilter(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Initial product count
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available")))
        initial_product_count = len(products)
        print(f"Initial product count: {initial_product_count}")

        # Find and click the "Brand A" checkbox
        try:
            brand_a_checkbox_label = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[contains(text(), 'Brand A')]//input[@type='checkbox']"))
            )
            brand_a_checkbox_label.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        time.sleep(2)

        # Get product count after applying filter
        products_filtered = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available")))
        filtered_product_count = len(products_filtered)
        print(f"Product count after filtering by Brand A: {filtered_product_count}")
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after filtering")

        # Uncheck "Brand A"
        try:
            brand_a_checkbox_label = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[contains(text(), 'Brand A')]//input[@type='checkbox']"))
            )
            brand_a_checkbox_label.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox to uncheck: {e}")

        time.sleep(2)

        # Get product count after removing filter
        products_unfiltered = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available")))
        unfiltered_product_count = len(products_unfiltered)
        print(f"Product count after removing Brand A filter: {unfiltered_product_count}")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count should return to initial count after removing filter")

        # Price filter interaction - This is a placeholder, as the provided HTML doesn't include details for slider interaction
        # In a real scenario, you'd need to identify the slider element and use ActionChains to move it.
        # Example (requires proper element identification):
        # slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter-slider")))
        # action = ActionChains(driver)
        # action.drag_and_drop_by_offset(slider, 50, 0).perform() # Move slider by 50 pixels
        # time.sleep(2) # Wait for products to update

if __name__ == "__main__":
    unittest.main()