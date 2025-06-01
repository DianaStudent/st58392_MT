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

        # Find the Brand A checkbox and click it
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click Brand A checkbox: {e}")

        time.sleep(2)

        # Get product count after Brand A filter
        products_after_brand_a = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        product_count_after_brand_a = len(products_after_brand_a)

        # Uncheck Brand A
        try:
            brand_a_checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(brand_a_checkbox_locator)
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click Brand A checkbox to uncheck: {e}")

        time.sleep(2)

        # Get product count after unchecking Brand A
        products_after_uncheck = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        product_count_after_uncheck = len(products_after_uncheck)

        # Assert that the product count changed after applying and removing the filter
        self.assertNotEqual(initial_product_count, product_count_after_brand_a, "Product count should change after applying Brand A filter.")
        self.assertNotEqual(product_count_after_brand_a, product_count_after_uncheck, "Product count should change after unchecking Brand A filter.")
        self.assertEqual(initial_product_count, product_count_after_uncheck, "Product count should return to initial count after unchecking Brand A filter.")

        #Price filter
        price_filter_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        try:
            price_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(price_filter_locator)
            )
            initial_price = price_filter.text
        except Exception as e:
            self.fail(f"Could not find price filter: {e}")

        # Change price range
        # No slider to interact with, so skipping this step

if __name__ == "__main__":
    unittest.main()