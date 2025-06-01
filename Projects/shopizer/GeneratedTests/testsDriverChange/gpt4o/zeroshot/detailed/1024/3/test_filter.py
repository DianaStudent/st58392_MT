import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Accept cookies if the button exists
        try:
            accept_cookies_button = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found")

        # Filter by "Tables"
        try:
            tables_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables filter tab not found")

        # Wait for product grid to update and get product count
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        products_tables = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        self.assertGreater(len(products_tables), 0, "No products found after tables filter")
        self.assertEqual(len(products_tables), 1, "Expected 1 product after tables filter")

        # Filter by "Chairs"
        try:
            chairs_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs filter tab not found")

        # Wait for product grid to update and get product count
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        products_chairs = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        self.assertGreater(len(products_chairs), 0, "No products found after chairs filter")
        self.assertEqual(len(products_chairs), 3, "Expected 3 products after chairs filter")

        # Ensure the list is different from the "Tables" filter
        self.assertNotEqual(products_tables[0].get_attribute("href"), products_chairs[0].get_attribute("href"),
                            "Product lists should differ between 'Tables' and 'Chairs' filters")

        # Filter by "All"
        try:
            all_tab = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='all']"))
            )
            all_tab.click()
        except:
            self.fail("All filter tab not found")

        # Wait for product grid to update and get product count
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        products_all = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        self.assertGreater(len(products_all), 0, "No products found after all filter")
        self.assertEqual(len(products_all), 4, "Expected 4 products after all filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()