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

        # 3. Apply a price filter by navigating to a URL that includes the price parameter.
        #  Filter by price 15-50
        try:
            driver.get("http://max/search?q=book")

            # Verify the product list is updated
            product_grid_before = driver.find_element(By.CLASS_NAME, "product-grid").get_attribute('innerHTML')

            driver.get("http://max/search?q=book&price=15.00-50.00")

            product_grid_after = driver.find_element(By.CLASS_NAME, "product-grid").get_attribute('innerHTML')

            self.assertNotEqual(product_grid_before, product_grid_after, "Product grid has not been updated.")
        except NoSuchElementException:
            self.fail("Product grid not found.")

if __name__ == "__main__":
    unittest.main()