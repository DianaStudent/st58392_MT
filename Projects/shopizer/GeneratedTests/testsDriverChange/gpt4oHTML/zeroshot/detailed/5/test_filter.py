import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerFilterTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "root"))
        )

    def test_product_filters(self):
        driver = self.driver

        # Accept the cookies if the button is present
        try:
            accept_cookies = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except:
            self.fail("Accept cookies button not found or not clickable.")

        # Step 2: Apply the "Tables" filter
        try:
            tables_filter = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-tab-list .nav-item a[data-rb-event-key='tables']"))
            )
            tables_filter.click()
        except:
            self.fail("Tables filter tab not found or not clickable.")

        # Wait for product grid to update
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-content .fade.tab-pane.active.show .product-wrap-2"))
        )

        # Step 4: Store number of visible products for "tables"
        tables_products_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .fade.tab-pane.active.show .product-wrap-2"))
        self.assertEqual(tables_products_count, 1, "Number of products in 'Tables' filter should be 1.")

        # Step 5: Switch to the "Chairs" filter and wait for grid to refresh
        try:
            chairs_filter = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-tab-list .nav-item a[data-rb-event-key='chairs']"))
            )
            chairs_filter.click()
        except:
            self.fail("Chairs filter tab not found or not clickable.")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-content .fade.tab-pane.active.show .product-wrap-2"))
        )

        # Verify the product grid for "Chairs"
        chairs_products_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .fade.tab-pane.active.show .product-wrap-2"))
        self.assertEqual(chairs_products_count, 3, "Number of products in 'Chairs' filter should be 3.")
        self.assertNotEqual(tables_products_count, chairs_products_count, "Product count should differ from 'Tables' and 'Chairs' filters.")

        # Step 7: Click the "All" filter to reset
        try:
            all_filter = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-tab-list .nav-item a[data-rb-event-key='all']"))
            )
            all_filter.click()
        except:
            self.fail("All filter tab not found or not clickable.")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-content .fade.tab-pane.active.show .product-wrap-2"))
        )

        # Confirm that product list contains more items than after previous filters
        all_products_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .fade.tab-pane.active.show .product-wrap-2"))
        self.assertEqual(all_products_count, 4, "Number of products in 'All' filter should be 4.")
        self.assertGreater(all_products_count, chairs_products_count, "'All' filter should display more products than 'Chairs' filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()