from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get('http://max/')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()
    
    def test_product_filter(self):
        driver = self.driver

        # Navigate to the search page
        try:
            search_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
            search_link.click()
        except:
            self.fail("Search link not found")

        # Perform search with keyword 'book'
        try:
            search_input = self.wait.until(EC.element_to_be_clickable((By.ID, "q")))
            search_input.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, "search-button")
            search_button.click()
        except:
            self.fail("Search elements not found")

        # Apply price filter by navigating to specific URL
        driver.get('http://max/search?price=15-50')

        # Verify that the product grid is updated
        try:
            product_grid = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-wrapper")))
            products = product_grid.find_elements(By.CLASS_NAME, "product-item")
            self.assertTrue(len(products) > 0, "Product grid is not updated")
        except:
            self.fail("Product grid not updated or elements not found")

if __name__ == "__main__":
    unittest.main()