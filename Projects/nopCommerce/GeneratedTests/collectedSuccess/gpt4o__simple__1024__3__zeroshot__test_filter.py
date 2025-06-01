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
        self.driver.maximize_window()
        self.driver.get("http://max/")
    
    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        
        # Wait until search box is present
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search box not found")
        
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        
        # Search for the keyword "book"
        search_box.send_keys("book")
        search_button.click()

        # Wait until search results are loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results not loaded")
        
        # Apply price filter 0 to 25
        driver.get("http://max/search?q=book&from=0&to=25")

        # Verify the product grid updates correctly
        try:
            products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item"))
            )
            self.assertTrue(len(products) > 0, "No products found within the price range 0 to 25")
        except:
            self.fail("Product grid did not update after applying the filter")

if __name__ == "__main__":
    unittest.main()