from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies if present
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies_button.click()
        except:
            pass  # If the button is not found, assume cookies are already accepted

        # Initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, '.product-wrap-2')
        initial_product_count = len(initial_products)
        
        if initial_product_count == 0:
            self.fail("Initial product count is zero, no products displayed on home page.")

        # Click on 'Tables' filter tab
        tables_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]')))
        tables_tab.click()

        # Wait for the products to update
        wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, '.product-wrap-2')) != initial_product_count)
        
        # Verify that at least one product is displayed after filter is applied
        filtered_products = driver.find_elements(By.CSS_SELECTOR, '.product-wrap-2')
        if len(filtered_products) == 0:
            self.fail("No products displayed after applying filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()