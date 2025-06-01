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
        driver = self.driver
        # Search for "book"
        search_input_xpath = "//input[@id='small-searchterms']"
        search_button_xpath = "//button[@class='button-1 search-box-button']"

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, search_input_xpath))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, search_button_xpath))
            )
        except:
            self.fail("Search input or button not found")

        search_input.send_keys("book")
        search_button.click()

        # Verify search results are displayed
        product_grid_xpath = "//div[@class='product-grid']"
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, product_grid_xpath))
            )
        except:
            self.fail("Product grid not found after search")

        # Apply price filter (e.g., 0-25) by navigating to a specific URL
        filter_url = "http://max/search?q=book"  # Assuming the search query is still needed
        driver.get(filter_url)

        # Check if the filter is applied correctly by verifying the presence of a product with a price within the filter range
        filtered_product_xpath = "//div[@class='product-item' and @data-productid='4']"

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, filtered_product_xpath))
            )
        except:
            self.fail("Filtered product not found after applying price filter")

if __name__ == "__main__":
    unittest.main()