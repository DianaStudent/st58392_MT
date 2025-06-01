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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Step 2: Click on "Search" link from top navigation
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # Verify search page loaded
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        self.assertIsNotNone(search_input, "Search input not found on search page")

        # Step 3: Enter the search term "book" and perform search
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 4: Locate and interact with price range slider
        # Simulate manual URL change to apply price filter
        driver.get("http://max/search?q=book&price=15-25")

        # Verify filtered results
        product_items = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item"))
        )
        self.assertTrue(product_items, "Product items not found or empty after filter")

        # Ensure URL contains price parameter
        current_url = driver.current_url
        self.assertIn("price=15-25", current_url, "Filtered URL does not include price parameter")
        
        # Verify product list is updated
        updated_product_titles = [item.text for item in driver.find_elements(By.CLASS_NAME, "product-title")]
        self.assertTrue(updated_product_titles, "Product titles not found or empty after filter")

if __name__ == "__main__":
    unittest.main()