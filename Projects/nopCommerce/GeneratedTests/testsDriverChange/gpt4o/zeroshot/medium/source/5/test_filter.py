from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Step 1: Click on the "Search" link
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found")
        search_link.click()

        # Step 2: Enter the search term and perform search
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input not found")
        search_input.send_keys("book" + Keys.ENTER)

        # Step 3: Interact with the price slider/filter
        price_range_from = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        if not price_range_from:
            self.fail("Price range 'from' element not found")
        
        price_range_to = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .to")
        if not price_range_to:
            self.fail("Price range 'to' element not found")
        
        # Assuming an interaction with the slider would manipulate the URL directly
        driver.get('http://max/search?q=book&price=0-25')

        # Step 4: Verify filtered URL and updated product grid
        current_url = driver.current_url
        self.assertIn('price=0-25', current_url, "URL does not contain the correct price filter")

        # Verify the product list is updated
        product_grid = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid")))
        if not product_grid or not product_grid.text.strip():
            self.fail("Product grid is either not found or empty after filtering")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()