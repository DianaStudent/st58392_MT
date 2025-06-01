import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):
    URL = "http://localhost/"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.wait = WebDriverWait(self.driver, 20)
        
        # Accept Cookies
        try:
            cookie_button = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except Exception as e:
            self.fail(f"Cookie acceptance button not found: {e}")

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Apply "Tables" filter
        try:
            tables_tab = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Failed to click Tables filter: {e}")

        # Wait for product grid to update and verify number of products
        tables_products = self._get_visible_products()
        self.assertEqual(len(tables_products), 1, "Tables filter product count mismatch")

        # Switch to "Chairs" filter
        try:
            chairs_tab = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Failed to click Chairs filter: {e}")

        # Verify number of products for "Chairs"
        chairs_products = self._get_visible_products()
        self.assertEqual(len(chairs_products), 3, "Chairs filter product count mismatch")
        self.assertNotEqual(set(tables_products), set(chairs_products), "Product list did not change between Tables and Chairs")

        # Switch to "All" filter
        try:
            all_tab = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Failed to click All filter: {e}")

        # Verify number of products for "All"
        all_products = self._get_visible_products()
        self.assertEqual(len(all_products), 4, "All filter product count mismatch")
        self.assertGreaterEqual(len(all_products), len(tables_products), "All products should be equal or more than tables")
        self.assertGreaterEqual(len(all_products), len(chairs_products), "All products should be equal or more than chairs")

    def _get_visible_products(self):
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            visible_products = [product for product in products if product.is_displayed()]

            for product in visible_products:
                product_name = product.find_element(By.CSS_SELECTOR, "h3 a")
                self.assertTrue(product_name.is_displayed(), "Product name is not visible")
                self.assertNotEqual(product_name.text.strip(), "", "Product name is empty")

            return visible_products
        except Exception as e:
            self.fail(f"Failed to get visible products: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()