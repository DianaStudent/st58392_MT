from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_product_filters(self):
        # Apply "Tables" filter
        tables_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#tab-1']")))
        tables_tab.click()

        # Wait for product grid to update
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-grid > .product-item")))

        # Store number of visible products (1 product)
        initial_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid > .product-item"))))

        self.assertGreaterEqual(initial_products_count, 0, "No products found")

        # Switch to the "Chairs" filter and wait for grid to refresh (3 products)
        chairs_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#tab-2']")))
        chairs_tab.click()

        # Wait for product grid to update
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-grid > .product-item")))

        # Store number of visible products (3 products)
        new_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid > .product-item"))))
        
        self.assertGreater(new_products_count, initial_products_count, "Product count did not change after applying 'Chairs' filter")

        # Verify that the list of products is updated and different from the previous
        for product in WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid > .product-item"))):
            self.assertNotEqual(product.text, "", "Product text is empty")
            self.assertNotEqual(len(product.text), initial_products_count, "Product list has not changed")

        # Then click the "All" filter to reset (4 products)
        all_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#tab-3']")))
        all_tab.click()

        # Wait for product grid to update
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-grid > .product-item")))

        # Store number of visible products (4 products)
        new_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid > .product-item"))))
        
        self.assertGreater(new_products_count, initial_products_count, "Product count did not change after applying 'All' filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()