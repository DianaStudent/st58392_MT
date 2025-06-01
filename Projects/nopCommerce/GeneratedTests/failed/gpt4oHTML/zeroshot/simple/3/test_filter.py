from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestSearchFilter(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.url = "http://max/"  # Replace this with the actual base url

    def tearDown(self):
        # Quit the driver after test
        self.driver.quit()

    def test_search_and_filter(self):
        driver = self.driver
        
        # Step 1: Navigate to the base page
        driver.get(self.url)
        
        # Step 2: Locate and interact with the search input
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_input.send_keys("book")
        except Exception:
            self.fail("Search input not found.")
        
        # Step 3: Locate and click the search button
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except Exception:
            self.fail("Search button not found.")
        
        # Step 4: Apply the price filter by using a URL with query parameters
        driver.get(self.url + "/search?q=book&price_min=0&price_max=25")  # Example addition of URL parameters
        
        # Step 5: Check that products are visible within the price range
        try:
            products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "item-box"))
            )
            self.assertTrue(len(products) > 0, "No products found in the selected price range.")
        except Exception:
            self.fail("Products not found after applying price filter.")

# Run the tests
if __name__ == "__main__":
    unittest.main()