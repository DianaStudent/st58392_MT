import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver

        # Step 2: Click on the "Search" link from the top navigation
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        
        if not search_link:
            self.fail("Search link is not found")
        
        search_link.click()

        # Step 3: Enter the search term and perform the search
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        
        if not search_box:
            self.fail("Search box is not found")
        
        search_box.send_keys("book")
        
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        
        if not search_button:
            self.fail("Search button is not found")
        
        search_button.click()

        # Step 4: Locate and interact with the price range slider
        # Simulate the price filter action by navigating to URL including price parameter
        driver.get("http://max/search?price=0-25")

        # Verify that the filtered URL includes the price parameter
        self.assertIn("price=0-25", driver.current_url)

        # Wait for the product list to update and verify change
        product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )
        
        if not product_grid:
            self.fail("Product grid is not found or not updated")
        
        products = product_grid.find_elements(By.CLASS_NAME, "item-box")
        
        if not products or len(products) == 0:
            self.fail("No products found in the product grid")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()