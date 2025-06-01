import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # 1. Perform a product search using the query "book".
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-box-button"))
            )
        except Exception as e:
            self.fail(f"Search input or button not found: {e}")

        search_input.send_keys("book")
        search_button.click()

        # Verify that search results page is loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except Exception as e:
            self.fail(f"Search results not found: {e}")

        # 2. Apply a price filter by navigating to a URL that includes the price parameter.
        # Assuming the price filter changes the URL.  Since we don't have the exact URL,
        # we'll simulate navigating to a URL that we *expect* would filter results.
        # In a real test, you would likely interact with UI elements to apply the filter.

        # Check if price filter block exists
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-filters"))
            )
        except Exception as e:
            self.fail(f"Product filters block not found: {e}")

        # Simulate navigation to a filtered URL (0-15)
        driver.get("http://max/search?q=book&price=0-15")

        # 3. Confirm success by checking that the resulting product grid is updated.
        # Verify that the product grid is updated after applying the filter.
        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except Exception as e:
            self.fail(f"Product grid not found after filtering: {e}")

        # Check if the number of products is as expected.
        # Based on the provided HTML, after filtering 0-15, only one product should be displayed.
        product_items = driver.find_elements(By.CLASS_NAME, "product-item")
        self.assertEqual(len(product_items), 1, "Incorrect number of products after filtering.")

if __name__ == "__main__":
    unittest.main()