import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")
        
        # Accept cookies if present
        try:
            accept_button = self.wait.until(
                EC.presence_of_element_located((By.ID, 'rcc-confirm-button'))
            )
            accept_button.click()
        except:
            self.fail("Cookie acceptance button is missing or not clickable.")
    
    def test_filter_products(self):
        driver = self.driver

        # Helper function to get visible products
        def get_visible_products_count():
            try:
                product_elements = self.wait.until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-wrap-2'))
                )
                return len(product_elements)
            except:
                self.fail("Failed to locate product elements.")
        
        # Click on the "Tables" filter tab
        try:
            tables_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]'))
            )
            tables_tab.click()
        except:
            self.fail("Failed to click on the Tables filter tab.")
            
        # Wait for product grid to update and get product count
        tables_product_count = get_visible_products_count()
        self.assertEqual(tables_product_count, 1, 
                         "Unexpected product count after filtering by Tables.")

        # Click on the "Chairs" filter tab
        try:
            chairs_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="chairs"]'))
            )
            chairs_tab.click()
        except:
            self.fail("Failed to click on the Chairs filter tab.")

        # Wait for grid to refresh and get product count
        chairs_product_count = get_visible_products_count()
        self.assertEqual(chairs_product_count, 3, 
                         "Unexpected product count after filtering by Chairs.")
        self.assertNotEqual(tables_product_count, chairs_product_count, 
                            "Product list did not update between filters.")

        # Click on the "All" filter tab
        try:
            all_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="all"]'))
            )
            all_tab.click()
        except:
            self.fail("Failed to click on the All filter tab.")

        # Confirm that product list contains more items than previous filters
        all_product_count = get_visible_products_count()
        self.assertEqual(all_product_count, 4, 
                         "Unexpected product count when no filters are applied.")
        self.assertTrue(all_product_count >= tables_product_count and all_product_count >= chairs_product_count, 
                        "Product list was not as expected after selecting All filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()