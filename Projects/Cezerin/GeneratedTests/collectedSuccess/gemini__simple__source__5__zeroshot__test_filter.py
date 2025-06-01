import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        driver = self.driver

        # Function to count product cards
        def count_product_cards():
            product_elements = driver.find_elements(By.CSS_SELECTOR, ".products > .column")
            return len(product_elements)

        # Initial product count
        initial_product_count = count_product_cards()
        if initial_product_count == 0:
            self.fail("No products found initially.")

        # Find the "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
        except:
            self.fail("Brand A checkbox not found")

        # Click the "Brand A" checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Product count after filtering by Brand A
        filtered_product_count = count_product_cards()
        if filtered_product_count == 0:
            self.fail("No products found after filtering by Brand A.")

        # Uncheck the "Brand A" checkbox
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
        except:
            self.fail("Brand A checkbox not found to uncheck")
        brand_a_checkbox.click()
        time.sleep(2)

        # Product count after unchecking Brand A
        final_product_count = count_product_cards()

        # Assert that the product count changed after filtering and unfiltering
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filtering.")
        self.assertEqual(initial_product_count, final_product_count, "Product count is not the same after removing the filter.")

if __name__ == "__main__":
    unittest.main()