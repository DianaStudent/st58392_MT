import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookies_button.click()
        except Exception as e:
            self.fail(f"Cookies accept button is missing: {str(e)}")

        # Click on the "Tables" tab filter
        tables_filter = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='tables']")))
        tables_filter.click()

        # Wait for product grid to update
        product_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show")))

        # Store number of visible products (should be 1)
        products_list = product_grid.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        self.assertGreater(len(products_list), 0, "No products are displayed after applying 'Tables' filter.")
        num_products_tables = len(products_list)

        # Click on the "Chairs" tab filter
        chairs_filter = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='chairs']")))
        chairs_filter.click()

        # Wait for grid to refresh
        product_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show")))

        # Verify that the list of products is updated and different from the previous
        products_list = product_grid.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        self.assertGreater(len(products_list), 0, "No products are displayed after applying 'Chairs' filter.")
        num_products_chairs = len(products_list)
        self.assertNotEqual(num_products_tables, num_products_chairs, "Product count did not change between 'Tables' and 'Chairs' filters.")

        # Click on the "All" tab filter
        all_filter = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-rb-event-key='all']")))
        all_filter.click()

        # Confirm that product list contains more items than after previous filters
        product_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-pane.active.show")))
        products_list = product_grid.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        self.assertGreater(len(products_list), num_products_chairs, "Product count did not increase after applying 'All' filter.")

if __name__ == "__main__":
    unittest.main()