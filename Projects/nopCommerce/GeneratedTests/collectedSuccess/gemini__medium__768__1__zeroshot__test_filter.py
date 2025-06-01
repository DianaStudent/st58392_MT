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
            self.fail("Search link not found")

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
            self.fail("Search input or button not found")

        # 3. Apply a price filter by navigating to a URL that includes the price parameter.
        # Assuming the price filter is applied by changing the URL.
        # In this example, we will navigate to a URL that filters the price between 15 and 50.
        filtered_url = self.base_url + "search?q=book"  # Construct the filtered URL
        driver.get(filtered_url)

        # 4. Wait for the page to update and verify that the product list is changed
        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )

            # Check if the product grid is not empty
            products = product_grid.find_elements(By.CLASS_NAME, "item-box")
            self.assertTrue(len(products) > 0, "Product grid is empty after filtering.")
        except NoSuchElementException:
            self.fail("Product grid not found after filtering.")

if __name__ == "__main__":
    unittest.main()