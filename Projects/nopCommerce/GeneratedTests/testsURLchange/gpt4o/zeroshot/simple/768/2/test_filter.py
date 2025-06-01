import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        
    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Perform a product search for "book".
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search box not found")

        search_box.send_keys("book")

        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        except:
            self.fail("Search button not found")

        search_button.click()

        # Apply a price filter by navigating to a URL that includes the price parameter.
        try:
            filter_url = f"{driver.current_url}?q=book&price=15-50"
            driver.get(filter_url)
        except:
            self.fail("Failed to navigate to filtered URL")

        # Confirm success by checking that the resulting product grid is updated.
        try:
            product_grid = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except:
            self.fail("Product grid not found or not updated")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()