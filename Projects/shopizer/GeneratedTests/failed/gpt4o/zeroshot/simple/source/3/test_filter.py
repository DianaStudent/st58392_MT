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
        self.driver.get("http://localhost/home_page")

    def test_filter_products(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accepting cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except Exception as e:
            self.fail(f"Cookie accept button not found: {str(e)}")

        # Get product count before applying filter
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active .product-wrap-2"))

        # Click on the "Tables" filter tab
        try:
            tables_filter_tab = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item a[data-rb-event-key='tables']")))
            tables_filter_tab.click()
        except Exception as e:
            self.fail(f"Tables filter tab not found: {str(e)}")

        # Wait until filter is applied and check product count
        try:
            wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show")))
            filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2"))
            self.assertGreater(filtered_product_count, 0, "No products displayed after applying filter.")
            self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter.")
        except Exception as e:
            self.fail(f"Error after applying table filter: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()