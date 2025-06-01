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
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Search for "book"
        search_input_locator = (By.ID, "small-searchterms")
        search_button_locator = (By.CLASS_NAME, "search-box-button")

        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(search_input_locator)
            )
            search_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
        except:
            self.fail("Search input or button not found.")

        search_input.send_keys("book")
        search_button.click()

        # Verify that search results are displayed
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_grid_locator)
            )
        except:
            self.fail("Product grid not found after search.")

        # 2. Apply price filter (0-15)
        # Assuming the price filter is applied by navigating to a specific URL
        filtered_url = "http://max/search?q=book"  # Replace with the actual URL for applying the filter
        self.driver.get(filtered_url)

        # 3. Confirm that the product grid is updated
        # Check for a specific product that should be present after filtering
        filtered_product_locator = (By.XPATH, "//div[@class='product-item' and @data-productid='4']")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(filtered_product_locator)
            )
        except:
            self.fail("Filtered product not found after applying the price filter.")

if __name__ == "__main__":
    unittest.main()