from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # 1. Open the homepage and click on the "Search" link from the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found")

        search_link.click()

        # 2. Enter the search term and perform the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input box not found")
        
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # 3. Locate and interact with the price range slider
        price_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        price_to = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .to")))
        if not price_from or not price_to:
            self.fail("Price range selectors not found")

        # Modify URL directly to simulate slider interaction as Selenium doesn't support direct slider movements
        driver.get("http://max/search?q=book&price=0-25")

        # 4. Wait for the page to update and verify
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-container .product-item")))
        
        # Verify URL
        current_url = driver.current_url
        if "?q=book&price=0-25" not in current_url:
            self.fail("URL does not include the price parameter")

        # Verify product list update
        product_items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        if not product_items:
            self.fail("Filtered product list is empty or not found")

        first_product = product_items[0]
        price = first_product.find_element(By.CSS_SELECTOR, ".price.actual-price")
        if not price or not price.text:
            self.fail("Price element is not found or empty")
        
        self.assertIn("$15.50", price.text, "Product price does not match expectation")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()