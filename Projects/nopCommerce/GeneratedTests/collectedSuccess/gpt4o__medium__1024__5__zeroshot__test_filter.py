from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Search" link from the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found")
        search_link.click()

        # Enter the search term and perform the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input box not found")
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Wait for the search results to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        # Mimic sliding the price range slider by navigating to a URL
        filtered_url = "http://max/search?q=book&price=15-50"
        driver.get(filtered_url)

        # Wait for the page to update with the filtered results
        wait.until(EC.url_contains("price=15-50"))

        # Verify the URL includes the price parameter
        current_url = driver.current_url
        self.assertIn("price=15-50", current_url)

        # Verify the product list is changed
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        if not products or len(products) == 0:
            self.fail("No products found after applying filter")
        
        # Verify that filtered products are shown
        expected_product_prices = ["$50.00", "$15.50", "$25.60", "$25.50"]
        actual_product_prices = [p.text for p in driver.find_elements(By.CLASS_NAME, "actual-price")]
        self.assertTrue(any(price in actual_product_prices for price in expected_product_prices), 
                        "Expected filtered products are not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()