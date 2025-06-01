import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        # Initial product count
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        initial_product_count = len(products)
        print(f"Initial product count: {initial_product_count}")

        # Find and click the "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[text()='Brand A']/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Product count after applying "Brand A" filter
        products_after_filter = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        product_count_after_filter = len(products_after_filter)
        print(f"Product count after Brand A filter: {product_count_after_filter}")
        self.assertNotEqual(initial_product_count, product_count_after_filter, "Product count should change after applying Brand A filter.")


        # Uncheck "Brand A"
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Product count after removing "Brand A" filter
        products_after_remove_filter = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        product_count_after_remove_filter = len(products_after_remove_filter)
        print(f"Product count after removing Brand A filter: {product_count_after_remove_filter}")
        self.assertEqual(initial_product_count, product_count_after_remove_filter, "Product count should return to initial count after removing Brand A filter.")

    def test_price_filter(self):
        #Locate price filter elements
        price_filter_values_locator = (By.CSS_SELECTOR, ".price-filter-values")
        price_filter_values = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(price_filter_values_locator)
        )
        initial_text = price_filter_values.text
        print(f"Initial price range: {initial_text}")

        #Change price range
        #No slider available, so skipping the price filter test

if __name__ == "__main__":
    unittest.main()