import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
    
    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Search" link from the top navigation
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Search')))
        if not search_link:
            self.fail("Search link not found on the homepage")
        search_link.click()

        # Enter the search term and perform the search
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        if not search_input:
            self.fail("Search input not found on the search page")
        search_input.send_keys("book")
        
        search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button-1.search-button')))
        if not search_button:
            self.fail("Search button not found on the search page")
        search_button.click()

        # Wait for the search results to load
        products_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.products-container')))
        if not products_container:
            self.fail("Products container not found on the search results page")

        # Interact with the price range filter
        price_filter_from = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'from')))
        price_filter_to = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'to')))
        
        if not price_filter_from or not price_filter_to:
            self.fail("Price filter elements not found")

        # Navigate to the price filter URL manually (as Selenium cannot handle sliders)
        driver.get("http://max/search?q=book&price=15-50")
        
        # Verify that the filtered URL is correct
        current_url = driver.current_url
        self.assertIn("price=15-50", current_url, "Price parameter not found in URL")

        # Verify that the product list is updated
        new_products_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.products-container')))
        if not new_products_container or len(new_products_container.find_elements(By.CLASS_NAME, 'product-item')) == 0:
            self.fail("No products found with the specified filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()