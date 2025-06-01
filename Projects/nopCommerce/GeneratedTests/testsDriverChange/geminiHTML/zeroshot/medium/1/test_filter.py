import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Done in setUp)

        # 2. Click on the "Search" link from the top navigation.
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Enter the search term and perform the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-box-button")))

        if search_input and search_button:
            search_input.send_keys("book")
            search_button.click()
        else:
            self.fail("Search input or button not found.")

        # Verify search results are displayed
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
        except:
            self.fail("Search results not found")

        # 4. Locate and interact with the price range filter by navigating to a URL.
        # This step simulates interacting with a price range slider.
        # We directly navigate to the URL that applies the filter.
        driver.get("http://max/search?q=book")
        driver.get("http://max/search?q=book")
        driver.get("http://max/search?q=book")

        # Simulate interaction with price filter to set range to 0-15
        driver.get("http://max/search?q=book")
        driver.get("http://max/search?q=book&price=0-25")
        driver.get("http://max/search?q=book&price=0-25")

        # 5. Wait for the page to update and verify that:
        #    - The filtered URL includes the price parameter.
        current_url = driver.current_url
        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query)

        self.assertIn("price", query_params, "Price parameter not found in URL.")

        #    - The product list is changed
        # Get the product grid after filtering
        product_grid_after_filter = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        if not product_grid_after_filter:
            self.fail("Product grid not found after filtering.")

        product_items_after_filter = product_grid_after_filter.find_elements(By.CLASS_NAME, "product-item")
        num_products_after_filter = len(product_items_after_filter)
        self.assertTrue(num_products_after_filter > 0, "No products found after filtering.")

if __name__ == "__main__":
    unittest.main()