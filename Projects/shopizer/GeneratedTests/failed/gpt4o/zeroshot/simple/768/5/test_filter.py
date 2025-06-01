from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_product_filter(self):
        driver = self.driver

        # Accept the cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Failed to locate or click accept cookies button: {str(e)}")

        # Check initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, '.product-wrap-2')
        initial_product_count = len(initial_products)
        if initial_product_count == 0:
            self.fail("No products found initially!")

        # Click on the 'Tables' filter
        try:
            tables_filter = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]'))
            )
            tables_filter.click()
        except Exception as e:
            self.fail(f"Failed to locate or click tables filter: {str(e)}")

        # Wait for the filtered products to load and check product count
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.tab-pane.active.show'))
            )
            filtered_products = driver.find_elements(By.CSS_SELECTOR, '.product-wrap-2')
            filtered_product_count = len(filtered_products)
            self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")
        except Exception as e:
            self.fail(f"Failed to validate filtered products: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()