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
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except NoSuchElementException:
            self.fail("Search input or button not found.")

        # Verify search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results not displayed")

        # Get the initial product list
        initial_product_grid = driver.find_element(By.CLASS_NAME, "product-grid")
        initial_product_html = initial_product_grid.get_attribute('innerHTML')

        # 3. Apply a price filter by navigating to a URL that includes the price parameter.
        driver.get("http://max/search?q=book")
        driver.execute_script("window.location.href = 'http://max/search?q=book&price=15-50'")

        # Wait for the page to update
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )

        # Verify that the product list is changed
        final_product_grid = driver.find_element(By.CLASS_NAME, "product-grid")
        final_product_html = final_product_grid.get_attribute('innerHTML')

        self.assertNotEqual(initial_product_html, final_product_html, "Product list did not change after filtering.")

if __name__ == "__main__":
    unittest.main()