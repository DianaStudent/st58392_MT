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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the homepage.
        base_html = driver.page_source
        if not base_html:
            self.fail("Homepage is empty.")

        # 2. Click on the "Search" link from the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found.")

        # 3. Enter the search term and perform the search.
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button"))
            )
            search_button.click()
        except NoSuchElementException:
            self.fail("Search input or button not found.")

        # Wait for search results to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )

        search_results_html = driver.page_source
        if not search_results_html:
            self.fail("Search results are empty.")

        # 4. Apply a price filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")
        driver.get(self.base_url + "search?q=book&price=0-25")

        # 5. Wait for the page to update and verify that:
        #   - The filtered URL includes the price parameter.
        #   - The product list is changed
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )

        filtered_search_results_html = driver.page_source
        if not filtered_search_results_html:
            self.fail("Filtered search results are empty.")

        # Check if the product list is changed
        self.assertNotEqual(search_results_html, filtered_search_results_html, "Product list did not change after filtering.")

if __name__ == "__main__":
    unittest.main()