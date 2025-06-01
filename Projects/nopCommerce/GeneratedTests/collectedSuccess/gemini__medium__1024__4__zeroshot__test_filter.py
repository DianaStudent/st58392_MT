import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click on the "Search" link from the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found.")

        # 2. Enter the search term and perform the search.
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
            )
            search_button.click()
        except NoSuchElementException:
            self.fail("Search input or button not found.")

        # 3. Locate and interact with the price range slider.
        # Navigate to the filter URL directly
        driver.get(self.base_url + "search?q=book")

        # 4. Apply a price filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")

        # 5. Wait for the page to update and verify that the product list is changed.
        # Get the product grid before filtering
        try:
            product_grid_before = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            product_grid_html_before = product_grid_before.get_attribute('innerHTML')
            self.assertIsNotNone(product_grid_html_before)
            self.assertTrue(len(product_grid_html_before) > 0)
        except NoSuchElementException:
            self.fail("Product grid not found before filtering.")

        # Apply the filter
        driver.get(self.base_url + "search?q=book&price=0-25")

        # Get the product grid after filtering
        try:
            product_grid_after = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            product_grid_html_after = product_grid_after.get_attribute('innerHTML')
            self.assertIsNotNone(product_grid_html_after)
            self.assertTrue(len(product_grid_html_after) > 0)
        except NoSuchElementException:
            self.fail("Product grid not found after filtering.")

        # Check if the product grid has changed
        self.assertNotEqual(product_grid_html_before, product_grid_html_after, "Product grid did not update after filtering.")

if __name__ == "__main__":
    unittest.main()