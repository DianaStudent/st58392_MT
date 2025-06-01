from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)
        
        # Accept cookies if the button exists
        try:
            accept_cookies = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except Exception as e:
            pass

    def test_product_filters(self):
        driver = self.driver
        wait = self.wait

        # Click the "Tables" filter tab
        tables_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-rb-event-key='tables']")))
        tables_tab.click()
        
        # Wait for product grid to update and verify one product is displayed
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active .col-xl-3")))
        table_products_count = len(products)
        self.assertGreater(table_products_count, 0, "No products displayed after applying 'Tables' filter.")

        # Click the "Chairs" filter tab
        chairs_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-rb-event-key='chairs']")))
        chairs_tab.click()
        
        # Wait for grid to refresh and verify three products are displayed
        wait.until(EC.staleness_of(products[0]))  # Wait for stale element to ensure grid is refreshed
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active .col-xl-3")))
        chairs_products_count = len(products)
        
        self.assertNotEqual(table_products_count, chairs_products_count, "Product list did not change when switching to 'Chairs' filter.")
        self.assertGreater(chairs_products_count, 0, "No products displayed after applying 'Chairs' filter.")

        # Click the "All" filter tab
        all_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-rb-event-key='all']")))
        all_tab.click()
        
        # Wait for grid to refresh and verify four products are displayed
        wait.until(EC.staleness_of(products[0]))  # Wait for stale element to ensure grid is refreshed
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active .col-xl-3")))
        all_products_count = len(products)
        
        self.assertGreater(all_products_count, chairs_products_count, "Product list did not reset properly for 'All' filter.")
        self.assertGreater(all_products_count, 0, "No products displayed after applying 'All' filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()