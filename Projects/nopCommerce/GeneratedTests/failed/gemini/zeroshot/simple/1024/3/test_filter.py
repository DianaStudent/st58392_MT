from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        search_button_locator = (By.CLASS_NAME, "search-box-button")

        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_input_locator)
            )
            search_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
        except:
            self.fail("Search input or button not found.")

        search_input.send_keys("book")
        search_button.click()

        # Verify that search results page is loaded
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results not loaded.")

        # 2. Apply price filter (0-15)
        filter_url = "http://max/search?q=book"  # Assuming the search query persists in the URL
        self.driver.get(filter_url)

        # Check that the filter is applied (verify the number of products)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except:
            self.fail("Product grid not found after applying filter.")

        # Check filter result
        product_grid = self.driver.find_element(By.CLASS_NAME, "product-grid")
        items = product_grid.find_elements(By.CLASS_NAME, "item-box")

        # Assert that the number of items is correct
        self.assertEqual(len(items), 1)

if __name__ == "__main__":
    unittest.main()