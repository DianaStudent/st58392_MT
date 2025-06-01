import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BookSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")  # Base URL from html_data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_search_and_filter_books(self):
        driver = self.driver
        wait = self.wait

        # Locate search box and enter the query "book"
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
        except Exception:
            self.fail("Search box not found or not interactable.")

        # Click search button
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except Exception:
            self.fail("Search button not found or not clickable.")

        # Update the URL to apply a price filter
        price_filter_url = driver.current_url + "?price=0-25"
        driver.get(price_filter_url)

        # Verify the filtered results
        try:
            product_grid = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            items = product_grid.find_elements(By.CLASS_NAME, "item-box")
            self.assertTrue(len(items) > 0, "No products found in the specified price range.")
        except Exception:
            self.fail("Product grid not found or not updated with filtered results.")

    def tearDown(self):
        self.driver.quit()

# Run the test
if __name__ == "__main__":
    unittest.main()