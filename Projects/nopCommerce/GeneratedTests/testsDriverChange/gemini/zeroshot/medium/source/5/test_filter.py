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
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on the "Search" link from the top navigation.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found.")

        # Verify that the search page is loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-page"))
        )
        self.assertEqual(driver.current_url, self.base_url + "search")

        # 3. Enter the search term and perform the search.
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

        # Verify that search results are loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )

        # 4. Apply a price filter by navigating to a URL that includes the price parameter.
        driver.get(self.base_url + "search?q=book")
        driver.execute_script("window.location.href = '" + self.base_url + "search?q=book&price=0-25'")

        # 5. Wait for the page to update and verify that the product list is changed.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )

        # Verify that only one product is displayed after filtering
        product_grid = driver.find_element(By.CLASS_NAME, "product-grid")
        items = product_grid.find_elements(By.CLASS_NAME, "item-box")
        self.assertEqual(len(items), 1)

if __name__ == "__main__":
    unittest.main()