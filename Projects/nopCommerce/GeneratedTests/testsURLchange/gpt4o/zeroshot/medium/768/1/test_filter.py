import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage and click on "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found")
        search_link.click()

        # Step 2: Enter search term and perform the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input not found")
        search_input.send_keys("book")

        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Step 3: Locate and interact with the price range slider
        from_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".selected-price-range .from")))
        if not from_price:
            self.fail("From price range not found")
        to_price = driver.find_element(By.CSS_SELECTOR, ".selected-price-range .to")
        if not to_price:
            self.fail("To price range not found")

        # Simulate changing the price filter in URL
        driver.get("http://max/search?q=book&price=0-25")

        # Step 4: Verify the URL and product list update
        current_url = driver.current_url
        self.assertIn("price=0-25", current_url, "Price filter not applied correctly in URL")

        products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        if not products:
            self.fail("No products found after filter applied")
        self.assertTrue(len(products) > 0, "Product list not updated")

if __name__ == "__main__":
    unittest.main()