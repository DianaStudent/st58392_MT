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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        driver = self.driver

        # Initial product count
        products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        initial_product_count = len(products)
        print(f"Initial product count: {initial_product_count}")

        # Find and click the "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count after filtering by Brand A
        products_brand_a = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        brand_a_product_count = len(products_brand_a)
        print(f"Product count after filtering by Brand A: {brand_a_product_count}")
        self.assertNotEqual(initial_product_count, brand_a_product_count, "Product count should change after filtering by Brand A")

        # Uncheck "Brand A"
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count after unchecking Brand A
        products_after_uncheck = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .column.available"))
        )
        uncheck_product_count = len(products_after_uncheck)

        print(f"Product count after unchecking Brand A: {uncheck_product_count}")
        self.assertEqual(initial_product_count, uncheck_product_count, "Product count should return to initial after unchecking Brand A")

        #Price filter
        price_filter_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        price_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )
        self.assertIsNotNone(price_filter)

if __name__ == "__main__":
    unittest.main()