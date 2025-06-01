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
        driver = self.driver

        # Find the "Brand A" checkbox input element.
        try:
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='attribute']/div[contains(text(), 'Brand')]/following-sibling::label[1]/input[@type='checkbox']"))
            )
        except:
            self.fail("Could not find Brand A checkbox")

        # Get initial product count
        initial_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column')]")
        initial_product_count = len(initial_products)

        # Click the "Brand A" checkbox to apply the filter.
        brand_a_checkbox.click()

        # Wait for 2 seconds.
        time.sleep(2)

        # Get product count after filter applied
        filtered_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column')]")
        filtered_product_count = len(filtered_products)

        # Uncheck the "Brand A" checkbox to remove the filter.
        brand_a_checkbox.click()

        # Wait for 2 seconds.
        time.sleep(2)

        # Get product count after filter removed
        unfiltered_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div[contains(@class, 'column')]")
        unfiltered_product_count = len(unfiltered_products)

        # Assert that the number of visible product cards changes after applying and removing the filter.
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count did not revert after removing filter")

        # Price filter test (minimal, as slider interaction is complex)
        try:
            price_filter_left_handle = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
            )
        except:
            self.fail("Could not find price filter left handle")

if __name__ == "__main__":
    unittest.main()