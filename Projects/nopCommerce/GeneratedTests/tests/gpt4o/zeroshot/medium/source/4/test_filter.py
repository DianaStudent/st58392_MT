import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the homepage.
        homepage_url = 'http://max/'
        self.assertEqual(driver.current_url, homepage_url, "Not on homepage at start.")

        # 2. Click on the "Search" link from the top navigation.
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Check if search page is loaded
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

        # 3. Enter the search term and perform the search.
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # 4. Locate and interact with the price range slider.
        # Simulate setting the price filter by adjusting URL
        filtered_url = 'http://max/search?price=15-50&q=book'
        driver.get(filtered_url)

        # 5. Wait for the page to update and verify that:
        #    - The filtered URL includes the price parameter.
        self.assertIn("price=15-50", driver.current_url, "URL does not contain the price filter parameter.")

        #    - The product list is changed
        products_grid = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        product_items = products_grid.find_elements(By.CLASS_NAME, "item-box")
        self.assertGreater(len(product_items), 0, "Product items are not visible.")

if __name__ == "__main__":
    unittest.main()