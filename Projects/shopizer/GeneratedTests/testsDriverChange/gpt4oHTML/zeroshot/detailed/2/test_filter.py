import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterProductsTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/")  # Assuming localhost server

    def test_product_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Close cookie consent if exists
        try:
            consent_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            if consent_button.is_displayed():
                consent_button.click()
        except Exception:
            pass

        # Helper function to count visible products
        def count_visible_products():
            products = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            return len([p for p in products if p.is_displayed()])

        # Apply "Tables" filter by clicking the corresponding tab
        tables_tab = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='tables']"))
        )
        tables_tab.click()

        # Wait for product grid to update and check that at least one product is displayed
        product_count_tables = count_visible_products()
        self.assertGreaterEqual(product_count_tables, 1)

        # Store number of visible products after applying "Tables" filter
        self.assertEqual(product_count_tables, 1, "Tables filter did not result in 1 product being displayed")

        # Switch to the "Chairs" filter
        chairs_tab = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='chairs']"))
        )
        chairs_tab.click()

        # Wait for product grid to refresh and check that at least one product is displayed
        product_count_chairs = count_visible_products()
        self.assertGreaterEqual(product_count_chairs, 1)

        # Verify that the product list is updated and different from the previous
        self.assertNotEqual(product_count_tables, product_count_chairs, "No change in product count after switching to chairs filter")
        self.assertEqual(product_count_chairs, 3, "Chairs filter did not result in 3 products being displayed")

        # Click the "All" filter to reset
        all_tab = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='all']"))
        )
        all_tab.click()

        # Confirm that product list contains more items than after previous filters
        product_count_all = count_visible_products()
        self.assertGreaterEqual(product_count_all, 1)
        self.assertGreater(product_count_all, product_count_chairs, "All filter did not result in more products than chairs filter")
        self.assertEqual(product_count_all, 4, "All filter did not result in 4 products being displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()