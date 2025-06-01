from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage and navigate
        search_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Search'))
        )
        search_link.click()

        # Step 2: Enter search term and perform the search
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, 'q'))
        )
        search_input.send_keys('book')

        search_button = driver.find_element(By.CLASS_NAME, 'search-button')
        search_button.click()

        # Step 3: Interact with the price range slider
        # Simulate setting a price range by directly modifying the URL
        driver.get("http://max/search?q=book&price=0-25")

        # Step 4: Wait for the page to update and verify the changes
        price_range_from = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-filter .selected-price-range .from'))
        )
        price_range_to = driver.find_element(By.CSS_SELECTOR, '.product-filter .selected-price-range .to')

        if (not price_range_from or not price_range_from.text or
            not price_range_to or not price_range_to.text):
            self.fail("Price range filter elements are missing or empty.")

        filtered_url = driver.current_url
        self.assertIn("price=0-25", filtered_url, "Price filter not applied correctly in URL.")

        # Verify product list is changed
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-item'))
        )

        self.assertGreater(len(products), 0, "Product list not updated as expected after applying filter.")

    def tearDown(self):
        # Close the browser window and clean up
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()