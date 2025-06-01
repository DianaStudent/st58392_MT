from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable")

        # Verify and click 'Tables' tab
        try:
            tables_tab = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']/h4[text()='Tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found or not clickable")

        # Check at least one product appears
        try:
            product_items = wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            self.assertGreater(len(product_items), 0, "No products found for 'Tables' filter")
        except:
            self.fail("No products displayed after clicking 'Tables' filter")

        # Verify and click 'Chairs' tab
        try:
            chairs_tab = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']/h4[text()='Chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found or not clickable")

        # Check product list is updated
        try:
            updated_product_items = wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            self.assertGreater(len(updated_product_items), 0, "No products found for 'Chairs' filter")
            self.assertNotEqual(len(updated_product_items), len(product_items), "Product list did not update for 'Chairs'")
        except:
            self.fail("Product list not updated after clicking 'Chairs' filter")

        # Verify and click 'All' tab
        try:
            all_tab = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']/h4[text()='All']"))
            )
            all_tab.click()
        except:
            self.fail("'All' tab not found or not clickable")

        # Check full product list is shown
        try:
            all_product_items = wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
            )
            self.assertGreater(len(all_product_items), 0, "No products found for 'All' filter")
            self.assertGreater(len(all_product_items), len(updated_product_items), "Full product list not shown for 'All'")
        except:
            self.fail("Full product list not displayed after clicking 'All' filter")

if __name__ == "__main__":
    unittest.main()