import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            cookie_accept_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_accept_button.click()
        except:
            self.fail("Cookie accept button not found or not clickable")

        # Open the home page and check for main menu
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "main-menu")))
        except:
            self.fail("Main menu not found on the home page")

        # Apply the "Tables" filter
        try:
            tables_tab = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]'))
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found or not clickable")

        # Wait for product grid to update and verify products
        tables_products = self.get_products("Tables filter")
        self.assertEqual(len(tables_products), 1, "Incorrect number of products for Tables filter")

        # Store identifiers or count for table products
        tables_product_identifiers = {product.find_element(By.TAG_NAME, 'a').get_attribute('href') for product in tables_products}

        # Switch to the "Chairs" filter and wait for grid to refresh
        try:
            chairs_tab = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="chairs"]'))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found or not clickable")

        # Verify product list is updated and different
        chairs_products = self.get_products("Chairs filter")
        self.assertEqual(len(chairs_products), 3, "Incorrect number of products for Chairs filter")
        
        chairs_product_identifiers = {product.find_element(By.TAG_NAME, 'a').get_attribute('href') for product in chairs_products}
        self.assertTrue(tables_product_identifiers.isdisjoint(chairs_product_identifiers), "Product identifiers did not change after filter")

        # Click the "All" filter to reset
        try:
            all_tab = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="all"]'))
            )
            all_tab.click()
        except:
            self.fail("All tab not found or not clickable")

        # Confirm product list contains more items
        all_products = self.get_products("All filter")
        self.assertEqual(len(all_products), 4, "Incorrect number of products for All filter")

    def get_products(self, context):
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
            )
            self.assertGreater(len(products), 0, f"No products found for {context}")
            return products
        except:
            self.fail(f"Product grid did not update for {context}")
            return []

if __name__ == "__main__":
    unittest.main()