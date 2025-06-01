import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestSearchFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_search_and_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage.
        driver.get("http://max/") # Replace with actual base URL
        
        # Check if the Home link is present
        try:
            home_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Home page")))
        except TimeoutException:
            self.fail("Home page link not found.")

        # Step 2: Click on the "Search" link from the top navigation.
        try:
            search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
            search_link.click()
        except TimeoutException:
            self.fail("Search link not clickable.")

        # Step 3: Enter the search term and perform the search.
        try:
            search_input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
            search_input.clear()
            search_input.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, 'button-1.search-button')
            search_button.click()
        except (TimeoutException, NoSuchElementException):
            self.fail("Search input or button not found.")

        # Verify that search results are loaded
        try:
            products_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-grid')))
            products = products_grid.find_elements(By.CLASS_NAME, 'item-box')
        except TimeoutException:
            self.fail("Search results not loaded or product-grid not found.")
        
        initial_product_count = len(products)
        if initial_product_count == 0:
            self.fail("No products found after initial search.")

        # Step 4: Simulate filtering by price 0 to 25
        try:
            driver.get("http://max/") # Replace with actual URL for filtering
        except Exception as e:
            self.fail(f"Failed to navigate to filtered URL: {e}")

        # Step 5: Wait for the page to update and verify.
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-grid')))
            
            # Re-fetch product list after filtering
            updated_products_grid = driver.find_element(By.CLASS_NAME, 'product-grid')
            updated_products = updated_products_grid.find_elements(By.CLASS_NAME, 'item-box')
        except TimeoutException:
            self.fail("Filter not applied or product-grid not reloaded.")

        # Check if the product list is changed
        updated_product_count = len(updated_products)
        if updated_product_count == 0:
            self.fail("No products found after filter is applied.")
        
        self.assertLess(updated_product_count, initial_product_count, "Product list did not update as expected.")

if __name__ == "__main__":
    unittest.main()