from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        self.accept_cookies()

    def tearDown(self):
        self.driver.quit()

    def accept_cookies(self):
        try:
            accept_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            )
            accept_button.click()
        except:
            self.fail("Cookies accept button not found or clickable.")

    def test_product_filters(self):
        driver = self.driver
        wait = self.wait

        # Apply "Tables" filter
        try:
            tables_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found or clickable.")

        # Wait for tables products to load
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        self.assertEqual(len(products), 1, "There should be 1 product visible for tables filter.")

        # Store product identifiers
        tables_products_set = set(product.find_element(By.TAG_NAME, 'a').get_attribute('href') for product in products)

        # Switch to "Chairs" filter
        try:
            chairs_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found or clickable.")

        # Wait for chairs products to load
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        self.assertEqual(len(products), 3, "There should be 3 products visible for chairs filter.")

        # Store product identifiers and ensure difference
        chairs_products_set = set(product.find_element(By.TAG_NAME, 'a').get_attribute('href') for product in products)
        self.assertNotEqual(tables_products_set, chairs_products_set, "Products should differ between filters.")

        # Switch to "All" filter
        try:
            all_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='all']"))
            )
            all_tab.click()
        except:
            self.fail("All tab not found or clickable.")

        # Wait for all products to load
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        self.assertEqual(len(products), 4, "There should be 4 products visible for all filter.")

if __name__ == "__main__":
    unittest.main()