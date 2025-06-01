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
    
    def test_filter_tables(self):
        driver = self.driver
        wait = self.wait

        # Accept Cookies
        try:
            accept_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except Exception:
            self.fail("Accept cookies button not found or not clickable.")

        # Click on "Tables" filter
        try:
            tables_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception:
            self.fail("Tables filter tab not found or not clickable.")

        # Check that at least one product is displayed
        try:
            product_list = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            product_count_after_filter = len(product_list)
            self.assertGreater(product_count_after_filter, 0, "No products displayed after applying Tables filter.")
        except Exception:
            self.fail("Products not displayed correctly after applying Tables filter.")

    def test_filter_chairs(self):
        driver = self.driver
        wait = self.wait

        # Accept Cookies
        try:
            accept_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except Exception:
            self.fail("Accept cookies button not found or not clickable.")

        # Click on "Chairs" filter
        try:
            chairs_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception:
            self.fail("Chairs filter tab not found or not clickable.")

        # Check that at least one product is displayed
        try:
            product_list = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            product_count_after_filter = len(product_list)
            self.assertGreater(product_count_after_filter, 0, "No products displayed after applying Chairs filter.")
        except Exception:
            self.fail("Products not displayed correctly after applying Chairs filter.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()