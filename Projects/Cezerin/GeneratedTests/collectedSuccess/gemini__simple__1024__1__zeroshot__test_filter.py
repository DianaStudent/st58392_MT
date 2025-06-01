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
        products_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div")
        initial_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        initial_count = len(initial_products)

        # Find and click the "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute']/div[contains(text(), 'Brand')]/following-sibling::label[1]/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Get product count after Brand A filter
        filtered_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        filtered_count = len(filtered_products)

        # Assert that the product count has changed
        self.assertNotEqual(initial_count, filtered_count, "Product count should change after applying the filter")

        # Uncheck the "Brand A" checkbox
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Get product count after removing Brand A filter
        unfiltered_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        unfiltered_count = len(unfiltered_products)

        # Assert that the product count has changed back
        self.assertEqual(initial_count, unfiltered_count, "Product count should return to initial count after removing the filter")

        # Price filter
        price_filter_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        price_filter = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(price_filter_locator)
        )
        initial_price = price_filter.text

        # Change price
        # No slider to interact with, so we cannot change the price.

if __name__ == "__main__":
    unittest.main()