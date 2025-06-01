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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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

        # Find and click the "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Product count after applying "Brand A" filter
        products_filtered = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        filtered_product_count = len(products_filtered)

        # Uncheck "Brand A"
        brand_a_checkbox_uncheck = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox_uncheck.click()
        time.sleep(2)

        # Product count after removing "Brand A" filter
        products_unfiltered = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        unfiltered_product_count = len(products_unfiltered)

        # Assert that the product count changed after filtering and unfiltering
        self.assertNotEqual(initial_product_count, filtered_product_count)
        self.assertNotEqual(filtered_product_count, unfiltered_product_count)
        self.assertEqual(initial_product_count, unfiltered_product_count)

    def test_price_filter(self):
        # Initial product count
        products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        initial_product_count = len(products)

        # Change the price filter
        price_filter_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Price']/following-sibling::div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        price_filter = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )

        # Get the initial price
        initial_price = price_filter.text

        # Change the price
        self.driver.execute_script("arguments[0].innerText = '$967.00';", price_filter)
        time.sleep(2)

        # Product count after applying price filter
        products_filtered = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column"))
        )
        filtered_product_count = len(products_filtered)

        # Assert that the product count changed after filtering
        self.assertNotEqual(initial_product_count, filtered_product_count)

if __name__ == "__main__":
    unittest.main()