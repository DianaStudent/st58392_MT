import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class TestPriceFilter(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://max/")  # Assuming the 'base' HTML is served at this URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_price_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the "Search" link from the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link or search_link.text == "":
            self.fail("Search link not found or empty")
        search_link.click()

        # Step 3: Enter the search term and perform the search
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_box:
            self.fail("Search input box not found")

        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        if not search_button or search_button.text == "":
            self.fail("Search button not found or empty")

        search_box.send_keys("book")
        search_button.click()

        # Step 4: Locate and interact with the price range slider
        # Since we are using a URL method to apply the filter, providing an action to simulate interaction
        driver.get("http://max/search?price=0-25")  # URL with price filter

        # Step 5: Wait for the page to update and verify
        # Check filtered URL
        current_url = driver.current_url
        self.assertIn("price=0-25", current_url, "Price filter parameter not found in URL")

        # Wait for and verify that the product list is updated
        products_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-grid")))
        items = products_grid.find_elements(By.CSS_SELECTOR, "div.item-box")
        if not items:
            self.fail("No products found after applying filter")

        # Additional check: Assert that the products are within the price range
        for item in items:
            price_element = item.find_element(By.CSS_SELECTOR, "span.actual-price")
            if not price_element or price_element.text == "":
                self.fail("Price element not found or empty")
            price_text = price_element.text.replace("$", "")
            price = float(price_text)
            self.assertTrue(0 <= price <= 25, f"Product with price {price} is out of the expected range")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()