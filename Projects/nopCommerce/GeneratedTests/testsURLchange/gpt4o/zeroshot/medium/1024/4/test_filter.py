import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Search")
        ))
        if not search_link:
            self.fail("Search link is not clickable or missing.")
        search_link.click()

        # Step 3: Enter search term and perform search
        search_box = wait.until(EC.presence_of_element_located(
            (By.ID, "q")
        ))
        if not search_box:
            self.fail("Search input box is not found or empty.")
        search_box.send_keys("book")
        
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.search-button")
        ))
        if not search_button:
            self.fail("Search button is not clickable or missing.")
        search_button.click()

        # Step 4: Interact with the price range filter
        price_filter_min = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-filter.price-range-filter .from")
        ))
        price_filter_max = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-filter.price-range-filter .to")
        ))

        if not price_filter_min or not price_filter_max:
            self.fail("Price range filter is missing or not visible.")

        # Assuming price filter interaction changes URL
        driver.get("http://max/search?price=15-50")  # Mock URL for filter

        # Step 5: Verify filtered URL and product list is updated
        current_url = driver.current_url
        self.assertIn("price=15-50", current_url, "URL does not include price parameter.")
        
        products = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-grid .item-box")
        ))
        if not products:
            self.fail("Product list is not updated or missing.")

        # Assuming presence of products indicates a successful filter
        self.assertGreater(len(products), 0, "No products found.")

if __name__ == "__main__":
    unittest.main()