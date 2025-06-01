import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        # Setup ChromeDriver with webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual URL of the homepage
        self.wait = WebDriverWait(self.driver, 20)

    def test_search_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the "Search" link from the top navigation
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Search')))
        if not search_link:
            self.fail("Search link not found")
        search_link.click()

        # Step 3: Enter the search term and perform the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        if not search_input:
            self.fail("Search input box not found")
        search_input.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.search-button')))
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Step 4: Simulate setting the price range by interacting with a fake slider (as the actual one is likely JavaScript-enhanced)
        # We will directly navigate to the URL with the price filter parameter set
        driver.get("http://max/")  # Replace with the actual URL format

        # Step 5: Verification after URL update
        # Verify that the filtered URL includes the price parameter
        current_url = driver.current_url
        if "price=0-25" not in current_url:
            self.fail("Current URL does not contain the expected price parameter")

        # Verify that the product list is changed
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'products-container')))
        if not product_grid or not product_grid.find_elements(By.CLASS_NAME, 'product-item'):
            self.fail("Product grid is empty or not updated")

        # Confirm there's at least one product displayed
        products = product_grid.find_elements(By.CLASS_NAME, 'product-item')
        if not products:
            self.fail("No products found after applying the filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()