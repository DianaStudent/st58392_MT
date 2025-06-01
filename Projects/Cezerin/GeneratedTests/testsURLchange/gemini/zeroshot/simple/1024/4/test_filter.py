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
        products_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]")
        initial_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        initial_count = len(initial_products)

        # Find and click the "Brand A" checkbox
        brand_a_checkbox_locator = (By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']")
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()

        # Wait for the filter to apply
        time.sleep(2)

        # Get the updated product count
        filtered_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        filtered_count = len(filtered_products)

        # Assert that the product count has changed
        self.assertNotEqual(initial_count, filtered_count, "Product count should change after applying filter")

        # Uncheck the "Brand A" checkbox
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(brand_a_checkbox_locator)
        )
        brand_a_checkbox.click()

        # Wait for the filter to be removed
        time.sleep(2)

        # Get the product count after removing the filter
        unfiltered_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        unfiltered_count = len(unfiltered_products)

        # Assert that the product count has returned to the initial count
        self.assertEqual(initial_count, unfiltered_count, "Product count should return to initial count after removing filter")

    def test_price_filter(self):
        # Initial product count
        products_locator = (By.XPATH, "//div[@class='columns is-multiline is-mobile products']/div[contains(@class, 'column')]")
        initial_products = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(products_locator)
        )
        initial_count = len(initial_products)

        # Move the price slider
        # Note: This is a simplified example. Interacting with a slider accurately
        # requires more complex actions like click and drag, which are beyond the scope
        # of this example given the limited information about the slider's implementation.
        # This example just finds the price filter values and asserts they exist.
        price_filter_left_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']")
        price_filter_right_locator = (By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-right']")
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(price_filter_left_locator))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(price_filter_right_locator))

        # Verify that the price filter elements are present
        self.assertTrue(self.driver.find_element(*price_filter_left_locator).is_displayed())
        self.assertTrue(self.driver.find_element(*price_filter_right_locator).is_displayed())

if __name__ == "__main__":
    unittest.main()