import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SearchFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_search_and_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Navigate to the base page
        driver.get('http://max')  # Replace with actual base URL

        # Check presence of search box
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
        except:
            self.fail("Search box not found.")

        # Perform a product search with the query "book"
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, 'search-box-button')
        search_button.click()
        
        # Ensure search results are displayed by checking presence of product grid
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-grid')))
        except:
            self.fail("Product grid not found on search results page.")

        # Apply price filter by navigating to a URL with price parameters
        driver.get('http://max/search?q=book&price=0-25')  # Assuming that this is the correct filter URL

        # Verifying the filter results
        try:
            product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-grid')))
            products = product_grid.find_elements(By.CLASS_NAME, 'item-box')
            self.assertTrue(any(products), "No products found in filtered results.")
        except:
            self.fail("Product grid not found or no products after applying filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()