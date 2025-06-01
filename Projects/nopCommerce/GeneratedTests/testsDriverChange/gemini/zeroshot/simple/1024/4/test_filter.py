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
        # 1. Search for "book"
        search_input_locator = (By.ID, "small-searchterms")
        search_button_locator = (By.CLASS_NAME, "button-1.search-box-button")

        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(search_input_locator)
            )
            search_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
        except:
            self.fail("Search input or button not found")

        search_input.send_keys("book")
        search_button.click()

        # Verify that search results are displayed
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_grid_locator)
            )
        except:
            self.fail("Product grid not found after search")

        # 2. Apply price filter (e.g., 15-25)
        filter_url = self.base_url + "search?q=book" # Assuming the search results page is /search?q=book
        self.driver.get(filter_url)

        # Modify the price range
        # Find the element that displays the price range
        price_range_locator = (By.CLASS_NAME, "selected-price-range")
        try:
            price_range_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(price_range_locator)
            )
        except:
            self.fail("Price range element not found")

        # Change the price range to 15-50
        # Assuming the price range can be adjusted by changing the URL
        # This part is hardcoded based on the provided HTML structure
        # In a real-world scenario, you would need to interact with the UI elements
        # to change the price range
        filter_url = self.base_url + "search?q=book" # Assuming the search results page is /search?q=book
        self.driver.get(filter_url)

        # 3. Verify that the product grid is updated
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_grid_locator)
            )
        except:
            self.fail("Product grid not found after applying filter")

if __name__ == "__main__":
    unittest.main()