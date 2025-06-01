import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_product_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception:
            self.fail("Accept cookies button not found or not clickable")

        # Click on 'Tables' filter
        try:
            tables_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']")))
            tables_filter.click()
        except Exception:
            self.fail("Tables filter tab not found or not clickable")

        # Verify table filter applied and products loaded
        try:
            tables_products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")))
            self.assertTrue(len(tables_products) > 0, "No products displayed after filtering for tables")
        except Exception:
            self.fail("Table products not displayed after applying filter")

        # Click on 'Chairs' filter
        try:
            chairs_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']")))
            chairs_filter.click()
        except Exception:
            self.fail("Chairs filter tab not found or not clickable")

        # Verify chair filter applied and products loaded
        try:
            chairs_products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2")))
            self.assertTrue(len(chairs_products) > 0, "No products displayed after filtering for chairs")
        except Exception:
            self.fail("Chair products not displayed after applying filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()