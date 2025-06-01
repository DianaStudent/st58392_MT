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
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookie acceptance button is missing or not clickable.")

    def test_filter_tables(self):
        driver = self.driver
        
        # Initially find the count of all products displayed
        all_products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        initial_count = len(all_products)
        
        # Click on the 'Tables' filter tab
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables filter tab is missing or not clickable.")
        
        # Wait for the product list to update after filter
        updated_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        updated_count = len(updated_products)
        
        # Check that the product count changes
        self.assertNotEqual(initial_count, updated_count, "Product count should change after applying the filter.")
        
        # Check that at least one product is displayed
        self.assertGreater(updated_count, 0, "No products displayed after filter applied.")
            
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()