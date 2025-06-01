import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        self.accept_cookies()

    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not available: {e}")

    def test_product_filter(self):
        # click 'Tables' filter
        self.apply_filter("tables")
        product_count_tables = self.count_products()
        self.assertGreater(product_count_tables, 0, "No products displayed for 'Tables' filter")

        # click 'Chairs' filter
        self.apply_filter("chairs")
        product_count_chairs = self.count_products()
        self.assertGreater(product_count_chairs, 0, "No products displayed for 'Chairs' filter")
        self.assertNotEqual(product_count_tables, product_count_chairs, "Product counts should differ between filters")

        # click 'All' filter
        self.apply_filter("all")
        product_count_all = self.count_products()
        self.assertGreater(product_count_all, max(product_count_tables, product_count_chairs), "Product count for 'All' should be the largest")

    def apply_filter(self, filter_key):
        filter_selector = f"a[data-rb-event-key='{filter_key}']"
        try:
            filter_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, filter_selector)))
            filter_tab.click()
            # Wait for the product grid to update, assuming active show indicates visibility
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")))
        except Exception as e:
            self.fail(f"Failed to apply filter {filter_key}: {e}")

    def count_products(self):
        try:
            # Count visible products
            products = self.driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
            return len(products)
        except Exception as e:
            self.fail(f"Failed to count products: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()