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
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver

        # Accept cookies if the button exists
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except Exception:
            self.fail("Cookies acceptance button is not available or click failed.")

        # Click "Tables" filter tab
        tables_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-link[data-rb-event-key='tables']"))
        )
        tables_tab.click()

        # Wait for product grid to update and store number of visible products
        product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .active .product-wrap-2"))
        )
        tables_products_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .active .product-wrap-2"))
        self.assertEqual(tables_products_count, 1, "Tables filter did not show correct number of products.")

        # Click "Chairs" filter tab
        chairs_tab = driver.find_element(By.CSS_SELECTOR, ".nav-link[data-rb-event-key='chairs']")
        chairs_tab.click()

        # Verify that list of products is updated and different from the previous
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .active .product-wrap-2"))
        )
        chairs_products_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .active .product-wrap-2"))
        self.assertEqual(chairs_products_count, 3, "Chairs filter did not show correct number of products.")
        self.assertNotEqual(tables_products_count, chairs_products_count, "Product list did not update.")

        # Click "All" filter tab to reset
        all_tab = driver.find_element(By.CSS_SELECTOR, ".nav-link[data-rb-event-key='all']")
        all_tab.click()

        # Confirm product list contains more items than after previous filters
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .active .product-wrap-2"))
        )
        all_products_count = len(driver.find_elements(By.CSS_SELECTOR, ".tab-content .active .product-wrap-2"))
        self.assertTrue(all_products_count > max(tables_products_count, chairs_products_count),
                        "All filter did not show more products than previous filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()