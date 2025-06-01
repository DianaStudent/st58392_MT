import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
    
    def test_product_filter(self):
        driver = self.driver
        
        try:
            # Wait for the search box to be present and enter the query "book"
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            
            # Wait for the search button to be present and click it
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
            
            # Wait for the result page with the price filter to be visible
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "selected-price-range"))
            )
            
            # Navigate directly to apply the price filter
            driver.get("http://max/search?q=book&price=0-25")
            
            # Wait for product grid to be updated based on the applied filter
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "products-container"))
            )
            
            # Check if there's at least one product in the grid
            items = product_grid.find_elements(By.CLASS_NAME, "product-item")
            self.assertTrue(len(items) > 0, "No products found after applying filter.")
        
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()