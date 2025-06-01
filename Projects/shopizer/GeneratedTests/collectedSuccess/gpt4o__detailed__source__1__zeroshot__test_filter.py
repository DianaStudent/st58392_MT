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

        # Accept cookies if the button is present
        try:
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except:
            pass

        # Apply "Tables" filter
        tables_tab = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='tables']"))
        )
        tables_tab.click()

        # Wait for product grid to update and get number of visible products
        self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        tables_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        self.assertEqual(len(tables_products), 1, "Tables filter should show 1 product.")

        # Switch to "Chairs" filter
        chairs_tab = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='chairs']"))
        )
        chairs_tab.click()

        # Ensure products update and differ from previous filter
        self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        chairs_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        self.assertEqual(len(chairs_products), 3, "Chairs filter should show 3 products.")
        self.assertNotEqual(tables_products, chairs_products, "Product list should be different for Chairs.")

        # Reset to "All" filter
        all_tab = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-rb-event-key='all']"))
        )
        all_tab.click()

        # Confirm the product list contains more items
        self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        all_products = driver.find_elements(By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")
        self.assertEqual(len(all_products), 4, "All filter should show 4 products.")
        self.assertNotEqual(chairs_products, all_products, "All filter product list should contain more items.")

if __name__ == "__main__":
    unittest.main()