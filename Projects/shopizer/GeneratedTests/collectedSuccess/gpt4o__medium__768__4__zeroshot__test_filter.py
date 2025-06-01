import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_products(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookies consent button not found.")

        # Check that page is loaded
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header area not loaded.")

        # Click on the "Tables" tab
        try:
            tables_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Tables']]"))
            )
            tables_tab.click()

            product_list = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            self.assertGreater(len(product_list), 0, "No products found after filtering by tables.")
        except:
            self.fail("Error interacting with Tables tab or no products loaded.")

        # Click on the "Chairs" tab
        try:
            chairs_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Chairs']]"))
            )
            chairs_tab.click()

            product_list = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            self.assertGreater(len(product_list), 0, "No products found after filtering by chairs.")
        except:
            self.fail("Error interacting with Chairs tab or no products loaded.")

        # Click "All" to remove the filter
        try:
            all_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='All']]"))
            )
            all_tab.click()

            product_list = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            self.assertGreater(len(product_list), 0, "No products found after removing filters.")
        except:
            self.fail("Error interacting with All tab or no products loaded.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()