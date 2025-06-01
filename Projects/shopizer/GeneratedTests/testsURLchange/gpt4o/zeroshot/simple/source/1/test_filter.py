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
        try:
            # Find and click the "Tables" filter tab
            tables_filter = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-item a[data-rb-event-key='tables']"))
            )
            tables_filter.click()
            
            # Check products display after filter
            filtered_products = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2"))
            )
            filtered_count = len(filtered_products)
            
            # Ensure there is at least one product displayed
            self.assertGreater(filtered_count, 0, "No products displayed after applying 'Tables' filter")

            # Reset the filter to "All"
            all_filter = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-item a[data-rb-event-key='all']"))
            )
            all_filter.click()
            
            # Check products display after removing filter
            all_products = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2"))
            )
            all_count = len(all_products)

            # Ensure the product count changes after applying filter
            self.assertNotEqual(filtered_count, all_count, "Product count did not change after filtering")
            
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()