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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        
        # Perform a product search using the query "book".
        try:
            search_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_input.send_keys("book")
            
            search_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search operation failed: {e}")

        # Apply a price filter by navigating to a URL that includes the price parameter.
        try:
            # Update the search URL with the price filter parameters.
            driver.get("http://max/search?q=book&price=0-25")
            
            # Confirm success by checking that the resulting product grid is updated.
            product_grid = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid .item-grid .item-box"))
            )
            
            # Check presence of a product within the specified price range
            products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
            self.assertTrue(len(products) > 0, "No products found in the filtered range.")
        except Exception as e:
            self.fail(f"Price filter operation failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()