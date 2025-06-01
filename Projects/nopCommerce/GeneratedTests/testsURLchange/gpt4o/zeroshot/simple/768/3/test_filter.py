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
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_products_by_price(self):
        driver = self.driver
        wait = self.wait

        # Search for the product "book"
        search_box = wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
        if not search_box:
            self.fail("Search box not found")
        search_box.send_keys("book")

        search_button = driver.find_element(By.CSS_SELECTOR, 'button.button-1.search-box-button')
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Wait for the search results page to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-page')))

        # Apply price filter through URL navigation
        driver.get("http://max/search?price=0-25")

        # Verify filtered search results
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'item-grid')))
        if not product_grid:
            self.fail("Product grid is not displayed properly after filtering")

        # Grab the price tags from the results to confirm they are within the desired range
        prices = product_grid.find_elements(By.CSS_SELECTOR, 'span.price.actual-price')
        filtered_prices = [float(price.text.replace('$', '')) for price in prices]
        
        # Check if all products are within the price range
        for price in filtered_prices:
            self.assertGreaterEqual(price, 0, "Price is less than expected range.")
            self.assertLessEqual(price, 25, "Price is greater than expected range.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()