from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Dismiss cookie consent if exists
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            if cookie_button:
                cookie_button.click()
        except:
            pass  # Continue if there's no cookie consent button

        # Step 2: Click on the "Tables" tab
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Tables']]"))
        )
        tables_tab.click()

        # Step 3: Verify at least one product appears
        table_products = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-hidden='false']//div[contains(@class, 'product-wrap-2')]"))
        )
        self.assertTrue(table_products, "No products are shown in the 'Tables' filter.")

        # Step 4: Click on the "Chairs" tab
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='Chairs']]"))
        )
        chairs_tab.click()

        # Step 5: Verify product list is updated
        chair_products = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-hidden='false']//div[contains(@class, 'product-wrap-2')]"))
        )
        self.assertNotEqual(
            len(table_products), len(chair_products), "Product list did not update when changing to 'Chairs' filter."
        )

        # Step 6: Click "All" to remove the filter
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[h4[text()='All']]"))
        )
        all_tab.click()

        # Step 7: Confirm the full list of products is shown
        all_products = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-hidden='false']//div[contains(@class, 'product-wrap-2')]"))
        )
        self.assertGreater(
            len(all_products), max(len(table_products), len(chair_products)),
            "The full product list is not displayed when 'All' is selected."
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()