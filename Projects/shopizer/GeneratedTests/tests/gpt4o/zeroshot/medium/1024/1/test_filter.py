import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
        # Accept cookies if displayed
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            pass

    def test_filter_products(self):
        # Click on the "Tables" tab to filter products
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tables"))
        )
        tables_tab.click()
        
        # Verify that at least one product appears
        products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        if not products:
            self.fail("No products displayed for 'Tables' filter")

        # Click on the "Chairs" tab to change the filter
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Chairs"))
        )
        chairs_tab.click()
        
        # Verify that product list is updated
        products_after_chair_filter = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        if not products_after_chair_filter:
            self.fail("No products displayed for 'Chairs' filter")

        self.assertNotEqual(len(products), len(products_after_chair_filter), 
                            "Product count did not change after applying 'Chairs' filter")

        # Click "All" to remove the filter
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "All"))
        )
        all_tab.click()
        
        # Confirm that the full list of products is shown
        all_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        if not all_products:
            self.fail("No products displayed when 'All' filter is applied")

        self.assertNotEqual(len(products_after_chair_filter), len(all_products), 
                            "Product count did not change after removing filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()