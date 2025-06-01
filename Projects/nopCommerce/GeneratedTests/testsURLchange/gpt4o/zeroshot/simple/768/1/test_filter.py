from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        
        try:
            # Wait and find the search input box
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )

            # Enter the search query
            search_box.send_keys("book")

            # Find and click the search button
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
            search_button.click()
            
            # Wait for the page to load and display the price filter
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-filters"))
            )

            # Navigate to the URL with the price filter applied
            driver.get("http://max/search?price=15-50")

            # Check if the product grid is updated
            updated_product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-box"))
            )
            
            # Check at least one product is displayed
            if not updated_product_grid:
                self.fail("Product grid did not update with the filtered results.")
        
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()