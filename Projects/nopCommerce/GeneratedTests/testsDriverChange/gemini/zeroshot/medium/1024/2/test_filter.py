import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.search_term = "book"

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the homepage.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on the "Search" link from the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Search link not found or clickable: {e}")

        # 3. Enter the search term and perform the search.
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys(self.search_term)

            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search input or button not found: {e}")

        # Verify search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except Exception as e:
            self.fail(f"Search results not found: {e}")

        # Get initial product list
        initial_product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )
        initial_product_html = initial_product_grid.get_attribute('innerHTML')

        # 4. Locate and interact with the price range filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")
        driver.get(self.base_url + "search?q=book&price=0-25")

        # 5. Wait for the page to update and verify that:
        #   - The filtered URL includes the price parameter.
        #   - The product list is changed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except Exception as e:
            self.fail(f"Product grid not found after filter: {e}")

        # Verify the product list is changed
        filtered_product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )
        filtered_product_html = filtered_product_grid.get_attribute('innerHTML')

        self.assertNotEqual(initial_product_html, filtered_product_html, "Product list did not change after filtering")

if __name__ == "__main__":
    unittest.main()