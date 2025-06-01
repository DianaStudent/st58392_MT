from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Accept Cookies
        try:
            cookies_btn = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookies_btn.click()
        except:
            self.fail("Cookies accept button not found")

        # Verify home page load
        featured_products_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-tab-list")))
        if not featured_products_section:
            self.fail("Featured products section not loaded")

        # Apply "Tables" filter
        tables_tab = driver.find_element(By.CSS_SELECTOR, "[data-rb-event-key='tables']")
        tables_tab.click()

        # Wait for update and verify product count
        tables_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active .product-wrap-2"))
        )

        self.assertEqual(len(tables_products), 1, "Tables filter should show 1 product")

        # Apply "Chairs" filter
        chairs_tab = driver.find_element(By.CSS_SELECTOR, "[data-rb-event-key='chairs']")
        chairs_tab.click()

        # Wait for update and verify product count
        chairs_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active .product-wrap-2"))
        )

        self.assertEqual(len(chairs_products), 3, "Chairs filter should show 3 products")
        self.assertNotEqual(tables_products, chairs_products, "Product lists should differ between tables and chairs")

        # Apply "All" filter
        all_tab = driver.find_element(By.CSS_SELECTOR, "[data-rb-event-key='all']")
        all_tab.click()

        # Wait for update and verify product count
        all_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tab-pane.active .product-wrap-2"))
        )

        self.assertEqual(len(all_products), 4, "All filter should show 4 products")
        self.assertTrue(len(all_products) > len(chairs_products), "All products view should have more products than chairs filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()