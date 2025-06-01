import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_filter_product(self):
        driver = self.driver
        wait = self.wait
        
        # Accept cookies if the popup is present
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception:
            self.fail("Cookie acceptance button not found.")
        
        # Get initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        initial_count = len(initial_products)

        # Click on the "Tables" filter tab
        try:
            tables_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']")))
            tables_tab.click()
        except Exception:
            self.fail("Tables filter tab not found.")
        
        # Wait for the filter to be applied and get updated product count
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")))
            filtered_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
            filtered_count = len(filtered_products)
        except Exception:
            self.fail("No products displayed after filtering.")

        # Check if product count has changed
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()