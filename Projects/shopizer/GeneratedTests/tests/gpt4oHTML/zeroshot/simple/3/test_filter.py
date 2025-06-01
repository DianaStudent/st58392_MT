import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class FilterProductsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Update with actual URL

    def test_filter_tables(self):
        driver = self.driver

        try:
            # Accept cookies
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()

            # Navigate to Tables filter tab
            tables_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-tab-list']/div/a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()

            # Wait for products to load
            products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .tab-pane.show .product-wrap-2"))
            )

            # Check if at least one product is displayed
            if len(products) == 0:
                self.fail("No products are displayed after filtering by tables.")
        
        except Exception as e:
            self.fail(f"Test failed due to an unexpected exception: {str(e)}")

    def test_filter_chairs(self):
        driver = self.driver

        try:
            # Accept cookies
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()

            # Navigate to Chairs filter tab
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-tab-list']/div/a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()

            # Wait for products to load
            products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .tab-pane.show .product-wrap-2"))
            )

            # Check if at least one product is displayed
            if len(products) == 0:
                self.fail("No products are displayed after filtering by chairs.")
        
        except Exception as e:
            self.fail(f"Test failed due to an unexpected exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()