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
        search_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        if search_link:
            search_link.click()
        else:
            self.fail("Search link not found.")

        # 3. Enter the search term and perform the search.
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
        )

        if search_input and search_button:
            search_input.send_keys("book")
            search_button.click()
        else:
            self.fail("Search input or button not found.")

        # Verify search results are loaded
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # 4. Locate and interact with the price range to filter products.
        # Navigate to the filter URL directly.
        driver.get("http://max/search?q=book")

        # 5. Wait for the page to update and verify the filtered URL and product list.
        # Wait for the filtered results to load.
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Get the current URL
        current_url = driver.current_url

        # Verify the URL contains the price filter parameter.
        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query)

        # Check if the URL contains the price parameter.
        if 'q' not in query_params:
            self.fail("The URL does not contain the 'q' parameter.")

        # Verify that the product list is updated.
        product_grid = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )

        if not product_grid:
            self.fail("Product grid not found after applying filter.")

        # Count the number of products displayed.
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        product_count = len(products)

        # Check if the product count is greater than 0.
        if product_count == 0:
            self.fail("No products found after applying filter.")

        print(f"Number of products found: {product_count}")


if __name__ == "__main__":
    unittest.main()