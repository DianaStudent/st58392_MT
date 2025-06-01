from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class FilterTest(unittest.TestCase):
    
    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Modify to the actual URL if needed
        self.driver.maximize_window()
        
    def tearDown(self):
        self.driver.quit()
    
    def test_filter_tables(self):
        driver = self.driver
        
        try:
            # Accept cookies
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Failed to find the 'accept cookies' button")
        
        try:
            # Click the "Tables" filter tab
            tables_filter_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-tab-list a[data-rb-event-key='tables']"))
            )
            tables_filter_tab.click()
        except:
            self.fail("Failed to find the 'Tables' filter tab")

        try:
            # Count products before the filter with 'All' tab
            all_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-tab-list a[data-rb-event-key='all']"))
            )
            all_tab.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.show"))
            )
            all_products = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.show .product-wrap-2")
            self.assertGreater(len(all_products), 0, "No products found under 'All' tab")
        
            # Apply "Tables" filter
            tables_filter_tab.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.show"))
            )
        
            # Count products after the filter
            filtered_products = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.show .product-wrap-2")
            self.assertGreater(len(filtered_products), 0, "No products displayed after filtering by 'Tables'")
            self.assertNotEqual(len(all_products), len(filtered_products), "Product count did not change after filtering")

        except:
            self.fail("An error occurred while checking filtered products")

if __name__ == "__main__":
    unittest.main()