import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        self.accept_cookies()

    def accept_cookies(self):
        try:
            accept_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_button.click()
        except Exception as e:
            self.fail(f"Cookie accept button not found or clickable: {e}")

    def test_product_filter(self):
        driver = self.driver

        # Check initial product count in the "All" category
        try:
            initial_products = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2"))
            )
        except Exception as e:
            self.fail(f"Initial products not found: {e}")

        initial_count = len(initial_products)
        if initial_count == 0:
            self.fail("No products displayed initially")

        # Select "Chairs" filter
        try:
            filter_chairs_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='chairs']")))
            filter_chairs_tab.click()
        except Exception as e:
            self.fail(f"Chair filter tab not found or clickable: {e}")

        # Check product count after applying filter
        try:
            post_filter_products = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2"))
            )
        except Exception as e:
            self.fail(f"Products not found after filtering: {e}")

        post_filter_count = len(post_filter_products)
        if post_filter_count == 0:
            self.fail("No products displayed after filtering")

        # Verify that the product count has changed
        self.assertNotEqual(initial_count, post_filter_count, "Product count did not change after applying filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()