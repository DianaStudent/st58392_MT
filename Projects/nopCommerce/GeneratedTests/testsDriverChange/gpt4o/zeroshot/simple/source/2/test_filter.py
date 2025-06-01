import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Find the search input
        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        if not search_input:
            self.fail("Search input not found")
        
        # Perform a search for "book"
        search_input.send_keys("book")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.search-box-button")))
        if not search_button:
            self.fail("Search button not clickable")
        search_button.click()

        # Apply price filter by navigating to specific URL
        driver.get("http://max/search?q=book&price=0-25")  # Example filter URL
        product_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid")))
        if not product_grid:
            self.fail("Product grid not updated after price filter")

        # Confirm there's at least one product in the grid
        products = product_grid.find_elements(By.CLASS_NAME, "product-item")
        if not products:
            self.fail("No products found after applying filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()