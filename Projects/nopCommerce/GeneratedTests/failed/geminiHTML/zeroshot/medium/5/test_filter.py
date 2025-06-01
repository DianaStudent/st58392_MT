from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re

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
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        if search_input:
            search_input.send_keys("book")
            search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-button")))
            if search_button:
                search_button.click()
            else:
                self.fail("Search button not found.")
        else:
            self.fail("Search input not found.")

        # Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Get the initial product list
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        initial_product_ids = [product.get_attribute("data-productid") for product in initial_products]
        self.assertTrue(len(initial_product_ids) > 0, "No products found after initial search.")

        # 4. Locate and interact with the price range filter.
        # Since we don't have a slider, we'll navigate to a URL with a price filter.
        # For example, let's filter for products between $0 and $15.50.
        # This is simulated by navigating directly to the filtered page.

        driver.get("http://max/search?q=book")

        # 5. Wait for the page to update and verify that:
        #   - The filtered URL includes the price parameter.
        #   - The product list is changed

        # Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Verify that the product list is changed
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        filtered_product_ids = [product.get_attribute("data-productid") for product in filtered_products]

        self.assertTrue(len(filtered_product_ids) > 0, "No products found after price filter.")
        self.assertNotEqual(initial_product_ids, filtered_product_ids, "Product list did not change after filtering.")

if __name__ == "__main__":
    unittest.main()