from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestFilterProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_products(self):
        driver = self.driver

        # Accept cookies if the button is present
        try:
            cookie_button = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            self.fail("Cookie accept button not found")

        # Click "Tables" tab to apply filter
        try:
            tables_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.nav-item > a[data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables filter tab not found")

        # Verify at least one product is displayed after applying "Tables" filter
        try:
            wait = WebDriverWait(driver, 20)
            products = wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2"))
            )
            self.assertGreater(len(products), 0, "No products found after applying Tables filter")
            number_of_tables = len(products)
        except:
            self.fail("No products displayed after selecting Tables filter")

        # Click "Chairs" tab to apply filter and verify products
        try:
            chairs_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.nav-item > a[data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs filter tab not found")

        # Ensure the product list updates
        try:
            wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2"))
            )
            products_chairs = driver.find_elements(By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2")
            self.assertGreater(len(products_chairs), 0, "No products found after applying Chairs filter")
            self.assertNotEqual(len(products_chairs), number_of_tables, "Products list did not update when switching to Chairs filter")
        except:
            self.fail("Products did not update after selecting Chairs filter")

        # Click "All" tab to reset filter and verify products
        try:
            all_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.nav-item > a[data-rb-event-key='all']"))
            )
            all_tab.click()
        except:
            self.fail("All filter tab not found")

        # Ensure the product list updates with more products after resetting
        try:
            wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2"))
            )
            products_all = driver.find_elements(By.CSS_SELECTOR, ".tab-content .active.show .product-wrap-2")
            self.assertGreater(len(products_all), 0, "No products found after applying All filter")
            self.assertGreater(len(products_all), max(number_of_tables, len(products_chairs)), "Product list did not reset to include all products")
        except:
            self.fail("Products did not update after selecting All filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()