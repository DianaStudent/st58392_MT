import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class FilterTest(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Assuming local server for testing
        self.wait = WebDriverWait(self.driver, 20)

        # Accept cookies to proceed
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception:
            self.fail("Cookie acceptance button not found!")

    def test_filter_process(self):
        driver = self.driver

        # Click on the "Tables" filter tab
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception:
            self.fail("Tables tab not found or not clickable!")

        # Verify at least one product is displayed under "Tables"
        tables_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        if not tables_products:
            self.fail("No products found after clicking Tables tab!")

        initial_product_count = len(tables_products)

        # Click on the "Chairs" filter tab
        try:
            chairs_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception:
            self.fail("Chairs tab not found or not clickable!")

        # Verify product list is updated under "Chairs"
        chairs_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        if not chairs_products or len(chairs_products) == initial_product_count:
            self.fail("Product list not updated after clicking Chairs tab!")

        # Click on the "All" tab to remove the filter
        try:
            all_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
        except Exception:
            self.fail("All tab not found or not clickable!")

        # Confirm the full list of products is shown
        all_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active.show .product-wrap-2"))
        )
        if not all_products or len(all_products) <= initial_product_count:
            self.fail("Full product list not displayed after clicking All tab!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()