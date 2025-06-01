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
        # Step 1: Perform a product search using the query "book"
        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys("book")
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button.search-box-button')
        search_button.click()

        # Validate results page loaded
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.page-title h1')))
        
        # Step 2: Apply a price filter by navigating to a URL that includes the price parameter
        self.driver.get("http://max/search?q=book&price=15-25")

        # Validate filter applied
        price_from = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.selected-price-range .from'))
        )
        price_to = self.driver.find_element(By.CSS_SELECTOR, 'div.selected-price-range .to')
        
        if not (price_from.text == "15" and price_to.text == "25"):
            self.fail("Price filter not applied correctly.")

        # Confirm success by checking that the resulting product grid is updated
        products_grid = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.products-wrapper div.product-grid'))
        )

        products = products_grid.find_elements(By.CSS_SELECTOR, 'div.product-item')
        if len(products) == 0:
            self.fail("No products found after applying filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()