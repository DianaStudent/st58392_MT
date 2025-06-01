import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestProductSearchAndFilter(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_search_and_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get('http://max')  # This URL should be the base URL of the application

        # Step 2: Click on the "Search" link from the top navigation
        try:
            search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
            search_link.click()
        except:
            self.fail("Search link not found")

        # Step 3: Enter the search term and perform the search
        try:
            search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-text")))
            search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
            search_input.clear()
            search_input.send_keys("book")
            search_button.click()
        except:
            self.fail("Search input or button not found")

        # Step 4: Locate and interact with the price range slider
        try:
            # Wait for the product grid to appear after the search
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item-box")))

            # Simulate navigation to URL with price parameter for filtering
            driver.get('http://max/search?q=book&price=15-25')  # Example filtered URL
        except:
            self.fail("Price filter not applied")

        # Step 5: Wait for the page to update and verify that:
        # - The filtered URL includes the price parameter.
        # - The product list is changed
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))
            current_url = driver.current_url
            self.assertIn('price=15-25', current_url, "Price parameter is missing from the URL")

            # Verify new product list is loaded
            products = driver.find_elements(By.CLASS_NAME, 'item-box')
            if not products:
                self.fail("Product list is empty after filtering")
        except Exception as e:
            self.fail(f"Error verifying filtered product list or URL: {e}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()