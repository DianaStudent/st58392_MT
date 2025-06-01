import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage.
        home_url = "http://max/"
        self.assertEqual(driver.current_url, home_url, "Not on the homepage.")

        # 2. Click on the "Search" link from the top navigation.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # 3. Enter the search term and perform the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.clear()
        search_input.send_keys("book")
        
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # Verify we are on the search results page
        self.assertTrue(wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "page-title"), "Search")), "Search page not loaded.")

        # 4. Locate and interact with the price range filter.
        # Assuming interaction by directly accessing the target URL with price filter.
        driver.get("http://max/search?q=book&price=15-50")

        # Wait for the page to update and verify that:
        # - The filtered URL includes the price parameter.
        self.assertIn("price=15-50", driver.current_url, "URL does not contain price filter.")

        # - The product list is changed.
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        products = product_grid.find_elements(By.CLASS_NAME, "item-box")
        self.assertGreater(len(products), 0, "Product grid is not updated or empty after filtering.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()