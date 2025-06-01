from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

        # Wait for the home page to load
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "root")))

            # Accept cookies
            accept_cookies_button = driver.find_element(By.ID, 'rcc-confirm-button')
            accept_cookies_button.click()

            # Click on the "Tables" filter tab
            tables_tab = driver.find_element(By.CSS_SELECTOR, ".nav-link[data-rb-event-key='tables']")
            tables_tab.click()

            # Wait for the product grid to update
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            visible_products_tables = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertTrue(len(visible_products_tables) > 0)

            # Store number of visible products (1 product)
            product_count_tables = len(visible_products_tables)
            self.assertEqual(product_count_tables, 1)

            # Switch to the "Chairs" filter
            chairs_tab = driver.find_element(By.CSS_SELECTOR, ".nav-link[data-rb-event-key='chairs']")
            chairs_tab.click()

            # Wait for the grid to refresh
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            visible_products_chairs = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertTrue(len(visible_products_chairs) > 0)

            # Verify that the list of products is updated and different from the previous
            product_count_chairs = len(visible_products_chairs)
            self.assertEqual(product_count_chairs, 3)
            self.assertNotEqual(product_count_tables, product_count_chairs)

            # Click the "All" filter to reset
            all_tab = driver.find_element(By.CSS_SELECTOR, ".nav-link[data-rb-event-key='all']")
            all_tab.click()

            # Wait for the grid to refresh
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            visible_products_all = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
            self.assertTrue(len(visible_products_all) > 0)

            # Confirm that product list contains more items than after previous filters
            product_count_all = len(visible_products_all)
            self.assertEqual(product_count_all, 4)

        except Exception as e:
            self.fail(f"Test failed due to missing element or unexpected error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()