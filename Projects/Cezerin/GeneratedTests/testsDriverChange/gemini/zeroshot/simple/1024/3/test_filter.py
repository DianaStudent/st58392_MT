import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Function to count product cards
        def count_product_cards():
            product_elements = driver.find_elements(By.CSS_SELECTOR, ".products .column[class*='is-']")
            return len(product_elements)

        # Initial count of product cards
        initial_product_count = count_product_cards()
        print(f"Initial product count: {initial_product_count}")

        # Find the "Brand A" checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']/input[@type='checkbox']"))
            )
        except:
            self.fail("Could not find 'Brand A' checkbox")

        # Click the "Brand A" checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Count product cards after applying the filter
        filtered_product_count = count_product_cards()
        print(f"Product count after filtering by Brand A: {filtered_product_count}")
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after filtering by Brand A")

        # Uncheck the "Brand A" checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]//label[text()='Brand A']/input[@type='checkbox']"))
            )
        except:
            self.fail("Could not find 'Brand A' checkbox")
        brand_a_checkbox.click()
        time.sleep(2)

        # Count product cards after removing the filter
        unfiltered_product_count = count_product_cards()
        print(f"Product count after removing Brand A filter: {unfiltered_product_count}")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count should revert to initial count after unfiltering Brand A")

        # Price filter
        # This is a placeholder, as interacting with the slider requires more complex actions
        # such as locating the slider handle and performing drag-and-drop.
        # The provided HTML doesn't contain enough information to implement the slider interaction.
        print("Price filter interaction placeholder.")

if __name__ == "__main__":
    unittest.main()