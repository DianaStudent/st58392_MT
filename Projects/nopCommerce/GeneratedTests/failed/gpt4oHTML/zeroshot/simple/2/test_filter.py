from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductSearchTest(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")  # Assume the base URL from "base" HTML

    def test_search_and_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Perform a product search using the query "book"
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
            search_box.send_keys("book")

            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
            search_button.click()

            # Verify that search page loaded
            search_input_box = wait.until(EC.element_to_be_clickable((By.ID, "q")))
            self.assertEqual(search_input_box.get_attribute("value"), "book", "Search input not found.")

        except Exception as e:
            self.fail(f"Failed during the search process: {str(e)}")
        
        # Apply a price filter by navigating to a URL that includes the price parameter
        try:
            # Navigating to the URL with filter applied
            driver.get("http://max/")  # example URL with filter

            # Verify that the price filter is applied, and product grid is updated
            selected_price_from = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from"))
            )
            selected_price_to = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .to")
            self.assertEqual(selected_price_from.text, "0", "Price filter 'from' not applied.")
            self.assertEqual(selected_price_to.text, "25", "Price filter 'to' not applied.")

            # Check the grid is updated
            products_grid = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".products-container .product-grid .item-grid"))
            )
            item_boxes = products_grid.find_elements(By.CLASS_NAME, "item-box")
            self.assertGreater(len(item_boxes), 0, "No products found in the grid after applying filter.")

        except Exception as e:
            self.fail(f"Failed during filter and grid verification: {str(e)}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()