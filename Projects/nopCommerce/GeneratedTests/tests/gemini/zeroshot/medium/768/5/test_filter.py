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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the homepage.
        base_html = driver.page_source
        if not base_html:
            self.fail("Base HTML is empty.")

        # 2. Click on the "Search" link from the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except:
            self.fail("Search link not found or not clickable.")

        search_page_html = driver.page_source
        if not search_page_html:
            self.fail("Search page HTML is empty.")

        # 3. Enter the search term and perform the search.
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-button"))
            )
            search_button.click()
        except:
            self.fail("Search input or button not found or not clickable.")

        search_results_html = driver.page_source
        if not search_results_html:
            self.fail("Search results HTML is empty.")

        # Verify search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results not displayed.")

        # 4. Apply a price filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")
        original_product_grid = driver.find_element(By.CLASS_NAME, "product-grid").get_attribute('innerHTML')

        driver.get(self.base_url + "search?q=book&price=0-25")

        # 5. Wait for the page to update and verify that the product list is changed.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except:
            self.fail("Product grid not found after filter applied.")

        filtered_product_grid = driver.find_element(By.CLASS_NAME, "product-grid").get_attribute('innerHTML')

        self.assertNotEqual(original_product_grid, filtered_product_grid, "Product list did not change after filtering.")

if __name__ == "__main__":
    unittest.main()