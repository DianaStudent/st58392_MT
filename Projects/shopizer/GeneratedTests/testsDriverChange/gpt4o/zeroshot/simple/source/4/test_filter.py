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

    def accept_cookies(self):
        try:
            accept_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click the accept cookies button: {e}")

    def test_filter_tables(self):
        self.filter_and_verify_product_count('tables')

    def test_filter_chairs(self):
        self.filter_and_verify_product_count('chairs')

    def test_filter_all(self):
        self.filter_and_verify_product_count('all')

    def filter_and_verify_product_count(self, filter_name):
        driver = self.driver
        wait = self.wait

        # Find the product tab list and click the filter tab
        try:
            filter_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f".nav-link[data-rb-event-key='{filter_name}']"))
            )
            filter_tab.click()
        except Exception as e:
            self.fail(f"Failed to find or click the {filter_name} filter tab: {e}")

        # Wait for the tab to activate
        try:
            active_tab = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f".tab-pane.active.show"))
            )
        except Exception as e:
            self.fail(f"The filter tab did not activate: {e}")

        # Ensure that at least one product is displayed after filtering
        try:
            products = active_tab.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertGreater(len(products), 0, "No products found after applying the filter.")
        except Exception as e:
            self.fail(f"Failed to find products after applying the filter: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()