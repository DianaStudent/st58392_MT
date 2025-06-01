import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterProductsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Placeholder, replace with actual URL if necessary
        self.wait = WebDriverWait(self.driver, 20)
        
        # Accept cookies
        try:
            cookies_accept_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookies_accept_button.click()
        except Exception:
            pass  # Cookies accept button may not always be present

    def test_filter_products(self):
        # Navigate to Tables tab
        tables_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[h4[text()='Tables']]")
            )
        )
        tables_tab.click()

        # Verify at least one product is displayed
        tables_products = self.get_visible_products()
        if not tables_products:
            self.fail("No products found in Tables tab")

        # Navigate to Chairs tab
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[h4[text()='Chairs']]")
            )
        )
        chairs_tab.click()

        # Verify product list is updated
        chairs_products = self.get_visible_products()
        if not chairs_products:
            self.fail("No products found in Chairs tab")

        # Navigate to All tab
        all_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[h4[text()='All']]")
            )
        )
        all_tab.click()

        # Verify the full list of products is displayed
        all_products = self.get_visible_products()
        if not all_products:
            self.fail("No products found in All tab")

        # Validate product count update
        self.assertNotEqual(len(tables_products), len(chairs_products), "Product count did not change when applying filters")
        self.assertNotEqual(len(chairs_products), len(all_products), "Product count did not change when removing filter")

    def get_visible_products(self):
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[contains(@class, 'product-wrap-2')]")
                )
            )
            return [product for product in products if product.is_displayed()]
        except Exception:
            return []

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()