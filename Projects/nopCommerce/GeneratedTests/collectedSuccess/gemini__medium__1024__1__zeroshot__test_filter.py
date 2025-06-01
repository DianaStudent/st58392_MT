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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the homepage (already done in setUp)

        # 2. Click on the "Search" link from the top navigation
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except TimeoutException:
            self.fail("Search link not found or not clickable.")

        # 3. Enter the search term and perform the search
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.clear()
            search_input.send_keys("book")

            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
            )
            search_button.click()

        except TimeoutException:
            self.fail("Search input or button not found.")

        # Verify that search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except TimeoutException:
            self.fail("Search results not displayed after search.")

        # Get the initial product list
        initial_product_grid = driver.find_element(By.CLASS_NAME, "product-grid")
        initial_product_html = initial_product_grid.get_attribute('innerHTML')

        # 4. Apply price filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")
        driver.get(self.base_url + "search?q=book&price=0-25")

        # 5. Wait for the page to update and verify the product list is changed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except TimeoutException:
            self.fail("Product grid not found after applying filter.")

        # Get the filtered product list
        filtered_product_grid = driver.find_element(By.CLASS_NAME, "product-grid")
        filtered_product_html = filtered_product_grid.get_attribute('innerHTML')

        # Assert that the product list has changed
        self.assertNotEqual(initial_product_html, filtered_product_html, "Product list did not change after applying filter.")

if __name__ == "__main__":
    unittest.main()