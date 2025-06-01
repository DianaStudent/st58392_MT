import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class FilterProductsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://yourwebsite.com")  # Replace with actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_products(self):
        driver = self.driver
        
        # Accept cookies if present
        try:
            accept_cookies_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass  # Element might not be present if cookies are already accepted
        
        # Click on the "Tables" tab
        tables_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']")))
        tables_tab.click()
        
        # Wait for products to refresh
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show")))
        
        # Verify the number of products is 1 after selecting Tables
        visible_products_after_tables = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
        self.assertEqual(len(visible_products_after_tables), 1, "Expected 1 product for 'Tables' filter")
        
        # Click on the "Chairs" tab
        chairs_tab = driver.find_element(By.XPATH, "//a[@data-rb-event-key='chairs']")
        chairs_tab.click()
        
        # Wait for products to refresh
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show")))
        
        # Verify the number of products is 3 after selecting Chairs
        visible_products_after_chairs = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
        self.assertEqual(len(visible_products_after_chairs), 3, "Expected 3 products for 'Chairs' filter")
        
        # Click on the "All" tab
        all_tab = driver.find_element(By.XPATH, "//a[@data-rb-event-key='all']")
        all_tab.click()
        
        # Wait for products to refresh
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show")))

        # Verify the number of products is 4 after selecting All
        visible_products_after_all = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
        self.assertEqual(len(visible_products_after_all), 4, "Expected 4 products for 'All' filter")

        # Ensure that the product count changes after applying filters
        self.assertTrue(len(visible_products_after_all) > len(visible_products_after_chairs), 
                        "Product count after 'All' should be greater than 'Chairs'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()