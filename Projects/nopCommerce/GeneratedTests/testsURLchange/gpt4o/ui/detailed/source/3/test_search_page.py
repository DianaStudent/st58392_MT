import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Verify header is visible
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertIsNotNone(header)
        
        # Verify footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertIsNotNone(footer)
        
        # Verify search input field is visible
        search_input = wait.until(EC.visibility_of_element_located((By.ID, 'q')))
        self.assertIsNotNone(search_input)
        
        # Verify search button is visible and clickable
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-button')))
        self.assertIsNotNone(search_button)
        
        # Verify search page title is visible
        page_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-title')))
        self.assertIsNotNone(page_title)
        
        # Verify product items are visible
        product_items = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'product-item')))
        self.assertTrue(len(product_items) > 0, "No product items found")

        # Interact with search button
        search_button.click()

        # Verify that the UI reacts visually, e.g., search results appear
        search_results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-results')))
        self.assertIsNotNone(search_results)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()