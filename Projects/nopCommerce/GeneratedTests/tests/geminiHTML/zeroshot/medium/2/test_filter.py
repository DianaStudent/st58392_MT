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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage (already done in setUp)

        # 2. Click on the "Search" link from the top navigation.
        try:
            search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found.")

        # 3. Enter the search term and perform the search.
        try:
            search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
            search_input.send_keys("book")
            search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button")))
            search_button.click()
        except NoSuchElementException:
            self.fail("Search input or button not found.")

        # Verify search results are displayed
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
        except NoSuchElementException:
            self.fail("Search results not displayed")

        # Get the initial list of products
        initial_product_ids = []
        try:
            product_items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
            for item in product_items:
                product_id = item.get_attribute("data-productid")
                initial_product_ids.append(product_id)
        except NoSuchElementException:
            self.fail("No products found before filtering.")

        # 4. Navigate to a URL that includes the price parameter to filter the results.
        driver.get("http://max/search?q=book&price=0-25")

        # 5. Wait for the page to update and verify the product list is changed.
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
        except NoSuchElementException:
            self.fail("Search results not displayed after filtering")

        # Verify that the product list is updated
        filtered_product_ids = []
        try:
            product_items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
            for item in product_items:
                product_id = item.get_attribute("data-productid")
                filtered_product_ids.append(product_id)
        except NoSuchElementException:
            self.fail("No products found after filtering.")

        self.assertNotEqual(initial_product_ids, filtered_product_ids, "Product list did not change after filtering.")

if __name__ == "__main__":
    unittest.main()