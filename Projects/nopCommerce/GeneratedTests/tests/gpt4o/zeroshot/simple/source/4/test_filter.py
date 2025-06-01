from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver
        
        # Wait for the search input and enter "book"
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_input.clear()
            search_input.send_keys("book")
            
            # Find and click the search button
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()

            # Check that the product grid is present
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-item"))
            )

            # Apply a price filter by navigating to a specific URL
            driver.get("http://max/search?q=book&from=15&to=50")

            # Verify that the filtered product grid is updated
            products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item"))
            )
            self.assertGreater(len(products), 0, "No products found")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()