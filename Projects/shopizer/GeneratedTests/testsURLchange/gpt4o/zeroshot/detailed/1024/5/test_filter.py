import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookie consent button not found.")

        # Step 1: Open the home page
        driver.get("http://localhost/")

        # Step 2: Apply the "Tables" filter
        try:
            tables_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='tables']"))
            )
            tables_filter.click()
        except:
            self.fail("Tables filter tab not found.")

        # Step 3: Wait for product grid to update
        table_products = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='tabpanel'].active.show .product-wrap-2"))
        )
        table_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div[role='tabpanel'].active.show .product-wrap-2"))
        if table_product_count == 0:
            self.fail("No products found for 'Tables' filter.")

        # Step 4: Store the number of visible products for Tables filter
        self.assertEqual(table_product_count, 1)

        # Step 5: Switch to "Chairs" filter
        try:
            chairs_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='chairs']"))
            )
            chairs_filter.click()
        except:
            self.fail("Chairs filter tab not found.")

        # Step 6: Wait for grid to refresh and verify the product count
        chairs_products = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='tabpanel'].active.show .product-wrap-2"))
        )
        chairs_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div[role='tabpanel'].active.show .product-wrap-2"))
        self.assertEqual(chairs_product_count, 3)

        # Step 7: Click "All" filter
        try:
            all_filter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='all']"))
            )
            all_filter.click()
        except:
            self.fail("All filter tab not found.")

        # Step 8: Confirm that product list contains more items
        all_products = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='tabpanel'].active.show .product-wrap-2"))
        )
        all_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div[role='tabpanel'].active.show .product-wrap-2"))
        self.assertEqual(all_product_count, 4)

if __name__ == "__main__":
    unittest.main()