from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestFiltering(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Assuming the URL is "http://localhost:8080"

    def test_filtering(self):
        # Apply "Tables" filter
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='filter-item filter-tables']"))).click()
        
        # Wait for product grid to update
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']")))

        # Store number of visible products (1 product)
        tables_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-grid']//a[@class='product-item-link']"))))
        
        self.assertGreater(tables_products_count, 0)  # Check that at least one product is displayed

        # Switch to the "Chairs" filter and wait for grid to refresh (3 products)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='filter-item filter-chairs']"))).click()
        
        # Wait for product grid to update
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']")))

        # Store number of visible products (3 products)
        chairs_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-grid']//a[@class='product-item-link']"))))
        
        self.assertGreater(chairs_products_count, 0)  # Check that at least one product is displayed

        # Verify that the list of products is updated and different from the previous
        self.assertNotEqual(tables_products_count, chairs_products_count)

        # Then click the "All" filter to reset (4 products)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='filter-item filter-all']"))).click()
        
        # Wait for product grid to update
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']")))

        # Store number of visible products (4 products)
        all_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-grid']//a[@class='product-item-link']"))))
        
        self.assertGreater(all_products_count, 0)  # Check that at least one product is displayed

        # Confirm that product list contains more items than after previous filters
        self.assertGreater(all_products_count, max(tables_products_count, chairs_products_count))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()