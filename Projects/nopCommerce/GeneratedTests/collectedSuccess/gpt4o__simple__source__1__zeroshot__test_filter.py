import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        try:
            # Locate search input on homepage
            search_input = wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
            search_button = driver.find_element(By.CSS_SELECTOR, '.button-1.search-box-button')
        except Exception as e:
            self.fail(f"Search input or button not found: {str(e)}")

        # Search for 'book'
        search_input.send_keys('book')
        search_button.click()

        try:
            # Wait for search page to load
            wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Search']")))
            
            # Apply price filter by navigating to URL with price parameters
            driver.get("http://max/search?q=book&price=0-25")
            
            # Verify results are updated
            result_items = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-grid')))
            self.assertTrue(result_items, "Product grid not found or not updated.")
        except Exception as e:
            self.fail(f"Product filter failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()