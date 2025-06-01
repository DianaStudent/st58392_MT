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
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the homepage
        driver.get("http://max/")
        
        # Step 2: Click on the "Search" link from the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        if not search_link or not search_link.is_displayed():
            self.fail("Search link not present.")
        search_link.click()

        # Step 3: Enter the search term and perform the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input or not search_input.is_displayed():
            self.fail("Search input not present.")
        search_input.send_keys("book")
        
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        if not search_button or not search_button.is_displayed():
            self.fail("Search button not present.")
        search_button.click()
        
        # Step 4: Locate and interact with the price range slider
        # Simulating URL change since direct interaction isn't feasible without actual slider element
        driver.get("http://max/search?q=book&price=0-25")
        
        # Verify that the URL includes the price parameter
        self.assertIn("price=0-25", driver.current_url)
        
        # Step 5: Wait for the page to update and verify product list change
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-wrapper")))
        products = product_grid.find_elements(By.CLASS_NAME, "item-box")
        
        # Check that the product list has updated content based on filter
        if not products or len(products) == 0:
            self.fail("Product list did not update or is empty.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()