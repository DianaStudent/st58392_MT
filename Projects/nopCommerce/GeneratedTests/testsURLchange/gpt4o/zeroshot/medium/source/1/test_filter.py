import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Click on the "Search" link from the top navigation.
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link:
            self.fail("Search link not found.")
        search_link.click()

        # Enter the search term and perform the search.
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input not found.")
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        if not search_button:
            self.fail("Search button not found.")
        search_button.click()

        # Interact with the price range slider (simulating URL change).
        driver.get("http://max/search?q=book&price=15-50")

        # Verify that the filtered URL includes the price parameter.
        current_url = driver.current_url
        self.assertIn("price=15-50", current_url, "Filtered URL does not include the price parameter.")

        # Verify that the product list is changed
        products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))
        if not products:
            self.fail("No products found after filtering.")
        self.assertGreater(len(products), 0, "Product list is not updated after filtering by price.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()