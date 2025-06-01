import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Perform a product search using the query "book".
        search_page_url = self.base_url + "search"
        self.driver.get(search_page_url)

        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-button"))
            )
        except:
            self.fail("Search input or button not found.")

        search_input.send_keys("book")
        search_button.click()

        # Verify that search results are displayed
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results not found after searching for 'book'.")

        # Get the initial product grid
        initial_product_grid = self.driver.find_element(By.CLASS_NAME, "product-grid").get_attribute('innerHTML')

        # 2. Apply a price filter by navigating to a URL that includes the price parameter.
        filter_url = self.base_url + "search?q=book"  # Base URL with search query
        filter_url += "&price=15-50"  # Add the price filter parameter
        self.driver.get(filter_url)

        # 3. Confirm success by checking that the resulting product grid is updated.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except:
            self.fail("Product grid not found after applying price filter.")

        # Get the updated product grid
        updated_product_grid = self.driver.find_element(By.CLASS_NAME, "product-grid").get_attribute('innerHTML')

        # Assert that the product grid has been updated
        self.assertNotEqual(initial_product_grid, updated_product_grid, "Product grid was not updated after applying price filter.")

if __name__ == "__main__":
    unittest.main()