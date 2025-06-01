import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.initial_product_count = 0

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        driver = self.driver

        # Get initial product count
        products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        self.initial_product_count = len(products)
        print(f"Initial product count: {self.initial_product_count}")

        # Find the "Brand A" checkbox and click it
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[text()='Brand A']/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox: {e}")

        time.sleep(2)

        # Get product count after Brand A filter
        products_after_brand_a = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        product_count_after_brand_a = len(products_after_brand_a)
        print(f"Product count after Brand A filter: {product_count_after_brand_a}")

        # Uncheck "Brand A"
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute'][div[@class='attribute-title'][text()='Brand']]/label[text()='Brand A']/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Brand A' checkbox to uncheck: {e}")

        time.sleep(2)

        # Get product count after unchecking Brand A filter
        products_after_uncheck = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        product_count_after_uncheck = len(products_after_uncheck)
        print(f"Product count after unchecking Brand A filter: {product_count_after_uncheck}")

        # Assert that the product count changed after applying and removing the filter
        self.assertNotEqual(self.initial_product_count, product_count_after_brand_a, "Product count should change after applying the filter")
        self.assertEqual(self.initial_product_count, product_count_after_uncheck, "Product count should return to initial value after removing the filter")

if __name__ == "__main__":
    unittest.main()