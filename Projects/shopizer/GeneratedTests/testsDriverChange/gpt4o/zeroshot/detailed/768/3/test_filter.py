import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filters(self):
        driver = self.driver
        wait = self.wait

        # Dismiss cookie consent if present
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Navigate to "Tables" filter
        tables_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.nav-link[data-rb-event-key="tables"]')))
        tables_tab.click()

        # Wait for product grid for "Tables" to update
        product_grid_tables = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.tab-content .fade.tab-pane .product-wrap-2')
        ))

        self.assertEqual(len(product_grid_tables), 1, "Expected 1 product, found a different count.")

        # Navigate to "Chairs" filter
        chairs_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.nav-link[data-rb-event-key="chairs"]')))
        chairs_tab.click()

        # Wait for product grid for "Chairs" to update
        product_grid_chairs = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.tab-content .fade.tab-pane.active.show .product-wrap-2')
        ))

        self.assertEqual(len(product_grid_chairs), 3, "Expected 3 products, found a different count.")
        
        # Ensure product identifiers differ
        product_ids_tables = [prod.find_element(By.TAG_NAME, "a").get_attribute("href") for prod in product_grid_tables]
        product_ids_chairs = [prod.find_element(By.TAG_NAME, "a").get_attribute("href") for prod in product_grid_chairs]

        self.assertNotEqual(product_ids_tables, product_ids_chairs, "Product identifiers should differ between filters.")

        # Navigate to "All" filter
        all_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.nav-link[data-rb-event-key="all"]')))
        all_tab.click()

        # Wait for product grid for "All" to update
        product_grid_all = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.tab-content .fade.tab-pane.active.show .product-wrap-2')
        ))

        self.assertEqual(len(product_grid_all), 4, "Expected 4 products, found a different count.")
        
        # Ensure more items in "All" filter than "Tables" or "Chairs"
        self.assertTrue(len(product_grid_all) > len(product_grid_chairs), "More items expected in 'All' than 'Chairs'.")
        self.assertTrue(len(product_grid_all) > len(product_grid_tables), "More items expected in 'All' than 'Tables'.")

if __name__ == "__main__":
    unittest.main()