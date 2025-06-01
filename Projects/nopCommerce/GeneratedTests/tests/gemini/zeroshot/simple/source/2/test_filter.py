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
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, search_input_xpath))
            )
            search_input.send_keys("book")
        except:
            self.fail("Search input field not found.")

        search_button_xpath = "//button[@class='button-1 search-box-button']"
        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, search_button_xpath))
            )
            search_button.click()
        except:
            self.fail("Search button not found or not clickable.")

        # Verify search results are displayed
        product_grid_xpath = "//div[@class='product-grid']"
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, product_grid_xpath))
            )
        except:
            self.fail("Product grid not found after search.")

        # Apply price filter (navigate to URL with price parameter)
        driver.get(self.base_url + "search?q=book")
        driver.get(self.base_url + "search?q=book&price=0-25")

        # Verify that the product grid is updated after applying the filter
        filtered_product_grid_xpath = "//div[@class='product-grid']"
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, filtered_product_grid_xpath))
            )
        except:
            self.fail("Product grid not found after applying filter.")

if __name__ == "__main__":
    unittest.main()