import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_tables(self):
        try:
            # Accept cookies
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()

            # Check initial product count
            initial_products = self.driver.find_elements(By.CLASS_NAME, "product-wrap-2")
            initial_count = len(initial_products)
            if initial_count == 0:
                self.fail("No initial products displayed.")

            # Click on 'Tables' filter tab
            tables_filter_tab = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]'))
            )
            tables_filter_tab.click()

            # Check filtered product count
            filtered_products = self.driver.find_elements(By.CLASS_NAME, "product-wrap-2")
            filtered_count = len(filtered_products)
            if filtered_count == 0:
                self.fail("No products displayed after filtering 'Tables'.")

            self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()