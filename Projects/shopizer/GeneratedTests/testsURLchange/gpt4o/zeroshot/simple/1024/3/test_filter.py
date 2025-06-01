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

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        product_tab_list_selector = ".product-tab-list .nav-item"

        # Click on the "Tables" filter tab
        tables_filter = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"{product_tab_list_selector}[data-rb-event-key='tables']"))
        )
        tables_filter.click()

        # Check for product count after applying the filter
        products_after_filter = self.get_product_count()

        # If no products found, fail the test
        if products_after_filter == 0:
            self.fail("No products displayed after applying the 'Tables' filter")

        # Click on the "Chairs" filter tab
        chairs_filter = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"{product_tab_list_selector}[data-rb-event-key='chairs']"))
        )
        chairs_filter.click()

        # Check for product count after applying the filter
        products_after_chairs_filter = self.get_product_count()

        # Ensure product count changes, indicating filter application is effective
        self.assertNotEqual(products_after_filter, products_after_chairs_filter,
                            "Product count did not change after applying 'Chairs' filter")

    def get_product_count(self):
        wait = self.wait
        tab_content_selector = ".tab-content .fade.tab-pane.active.show"
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"{tab_content_selector} .product-wrap-2"))
        )
        return len(products)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()