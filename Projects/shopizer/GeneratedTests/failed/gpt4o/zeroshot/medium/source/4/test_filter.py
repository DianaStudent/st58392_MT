from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()
    
    def element_exists(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element if element.text.strip() else None
        except:
            return None
    
    def test_product_filter(self):
        driver = self.driver
        
        # Check the initial state (home page)
        home_page_title = self.element_exists(By.TAG_NAME, "h2")
        if not home_page_title:
            self.fail("Home page did not load correctly.")
        
        # Click on the "Tables" tab
        tables_tab = self.element_exists(By.XPATH, "//a[@data-rb-event-key='tables']")
        if not tables_tab:
            self.fail("Tables tab is missing.")
        tables_tab.click()
        
        # Verify that at least one product appears
        tables_products = self.element_exists(By.CLASS_NAME, "product-wrap-2")
        if not tables_products:
            self.fail("No products found in the 'Tables' filter.")
        
        # Click on the "Chairs" tab
        chairs_tab = self.element_exists(By.XPATH, "//a[@data-rb-event-key='chairs']")
        if not chairs_tab:
            self.fail("Chairs tab is missing.")
        chairs_tab.click()
        
        # Verify that product list is updated
        chairs_products = self.element_exists(By.CLASS_NAME, "product-wrap-2")
        if not chairs_products:
            self.fail("No products found in the 'Chairs' filter.")
        
        # Click "All" to remove the filter
        all_tab = self.element_exists(By.XPATH, "//a[@data-rb-event-key='all']")
        if not all_tab:
            self.fail("'All' tab is missing.")
        all_tab.click()

        # Confirm that the full list of products is shown
        all_products = self.element_exists(By.CLASS_NAME, "product-wrap-2")
        if not all_products:
            self.fail("No products found in the 'All' filter.")

if __name__ == "__main__":
    unittest.main()