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
        self.driver.set_window_size(1200, 800)

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        # Initial product count
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        initial_product_count = len(products)

        # Find the Brand A checkbox
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
        )

        # Click the Brand A checkbox
        brand_a_checkbox.click()
        time.sleep(2)

        # Get the updated product count
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        filtered_product_count = len(products)

        # Uncheck the Brand A checkbox
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Get the product count after unchecking
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        unfiltered_product_count = len(products)

        # Assert that the product count changed after filtering and unfiltering
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after filtering.")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count should return to initial after unfiltering.")

    def test_price_filter(self):
        # Initial product count
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        initial_product_count = len(products)

        # Price filter
        price_filter_left_value = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
        )
        initial_price = price_filter_left_value.text

        # Change price filter
        new_price = "$967.00"
        # Wait for the products to update after price change
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"), new_price)
        )

        # Get the updated product count
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        filtered_product_count = len(products)

        # Assert that the product count changed after filtering
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count should change after filtering.")

if __name__ == "__main__":
    unittest.main()