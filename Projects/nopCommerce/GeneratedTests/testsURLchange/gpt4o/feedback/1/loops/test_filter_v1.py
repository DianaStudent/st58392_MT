from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class ProductFilterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver
        
        # Step 1: Click on the "Search" link
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Enter "book" in the search field and submit the search
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 3: Wait for the search results to load
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))

        # Step 4: Locate and interact with the price range slider
        slider_handle_right = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]"
        )))

        # Move the right slider handle
        ActionChains(driver).drag_and_drop_by_offset(slider_handle_right, -50, 0).perform()

        # Wait for the filtering to apply
        filtered_products = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item")))

        # Step 5: Confirm that the product grid updates after slider movement
        product_grid = driver.find_elements(By.CLASS_NAME, "product-item")
        if not product_grid:
            self.fail("Product grid did not update or is empty after applying filter.")

        self.assertTrue(any(product.is_displayed() for product in product_grid), 
                        "No products are visible in the filtered results.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()