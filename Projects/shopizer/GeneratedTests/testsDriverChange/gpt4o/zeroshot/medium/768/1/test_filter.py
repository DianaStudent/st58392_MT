from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_product_filters(self):
        driver = self.driver
        
        # Verify home page is loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-tab-list .nav-link"))
            )
        except TimeoutException:
            self.fail("Home page didn't load correctly - product tab list is missing.")
        
        # Function to verify at least one product appears
        def verify_products_displayed():
            try:
                products = self.wait.until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
                )
                self.assertGreater(len(products), 0, "No products are displayed.")
            except TimeoutException:
                self.fail("Products did not appear.")
        
        # Step 2: Click on the "Tables" tab to filter products
        tables_tab = driver.find_element(By.XPATH, "//a[h4[text()='Tables']]")
        tables_tab.click()
        verify_products_displayed()

        # Step 4: Click on the "Chairs" tab to change the filter
        chairs_tab = driver.find_element(By.XPATH, "//a[h4[text()='Chairs']]")
        chairs_tab.click()
        verify_products_displayed()
        
        # Step 6: Click "All" to remove the filter
        all_tab = driver.find_element(By.XPATH, "//a[h4[text()='All']]")
        all_tab.click()
        verify_products_displayed()


if __name__ == "__main__":
    unittest.main()