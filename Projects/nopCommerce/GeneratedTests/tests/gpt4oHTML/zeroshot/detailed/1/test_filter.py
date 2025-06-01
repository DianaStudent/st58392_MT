import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class SearchFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # Replace with actual home page URL
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_search_and_filter_by_price(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        
        # Step 3: Enter "book" in the search field and submit
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input field not found.")

        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.search-button")
        search_button.click()
        
        # Step 4: Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
        
        # Step 5: Locate and interact with the price range slider
        # Assuming sliders have assigned IDs or unique classes
        price_filter_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-range-filter .from")))
        price_filter_to = driver.find_element(By.CSS_SELECTOR, ".price-range-filter .to")
        
        if not price_filter_from or not price_filter_to:
            self.fail("Price filter elements not found.")
        
        # Utilize ActionChains to mimic slider manipulation
        actions = ActionChains(driver)
        price_filter_from_elem = driver.find_element(By.CSS_SELECTOR, ".filter-content .from")
        actions.click_and_hold(price_filter_from_elem).move_by_offset(-50, 0).release().perform()  # Adjust -50 as needed
        
        # Wait dynamically for product grid update
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-container")))
        
        # Step 6: Confirm the product grid updates and at least one product is shown
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        
        if products:
            self.assertTrue(len(products) > 0, "Filtered products found.")
        else:
            self.fail("No products found in filtered results.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()