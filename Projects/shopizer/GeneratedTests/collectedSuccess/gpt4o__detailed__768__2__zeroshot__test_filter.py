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
        
    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Click on the "Tables" filter
        tables_tab = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='tables']"))
        )
        tables_tab.click()

        # Wait for product grid to update and store the number of visible products
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        tables_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        tables_product_count = len(tables_products)
        
        # Ensure at least one product is displayed
        if tables_product_count == 0:
            self.fail("No products displayed for 'Tables' filter")

        # Click on the "Chairs" filter
        chairs_tab = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='chairs']"))
        )
        chairs_tab.click()

        # Wait for product grid to update
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        chairs_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        chairs_product_count = len(chairs_products)
        
        # Ensure at least one product is displayed and list is different from the previous
        if chairs_product_count == 0:
            self.fail("No products displayed for 'Chairs' filter")
        if chairs_product_count == tables_product_count:
            self.fail("Product list did not update when switched to 'Chairs' filter")

        # Click on the "All" filter
        all_tab = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='all']"))
        )
        all_tab.click()

        # Wait for product grid to update
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        all_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        all_product_count = len(all_products)
        
        # Ensure product list contains more items than after previous filters
        if all_product_count <= chairs_product_count:
            self.fail("Product list did not reset to show more items after 'All' filter")

if __name__ == "__main__":
    unittest.main()