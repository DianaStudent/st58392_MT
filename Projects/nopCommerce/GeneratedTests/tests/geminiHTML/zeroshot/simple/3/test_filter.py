import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Search for "book"
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-box-button"))
            )
        except TimeoutException:
            self.fail("Search input or button not found")

        search_input.send_keys("book")
        search_button.click()

        # Verify search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except TimeoutException:
            self.fail("Search results not found")

        # Apply price filter (simulating navigation to a filtered URL)
        driver.get("http://max/search?q=book&price=0-25")

        # Verify that the price range is correctly displayed
        try:
            price_range = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "selected-price-range"))
            )
            self.assertIn("0", price_range.text)
            self.assertIn("25", price_range.text)
        except TimeoutException:
            self.fail("Price range not found or incorrect")

        # Verify that the product grid is updated after filtering
        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            # Check for a specific product that should be present after filtering.
            # This assumes that after filtering for 0-25, "Book4" will be present.
            book4_element = driver.find_element(By.XPATH, "//a[@href='/book4']")
            self.assertIsNotNone(book4_element)
        except TimeoutException:
            self.fail("Product grid not updated or expected product not found after filtering")

if __name__ == "__main__":
    unittest.main()