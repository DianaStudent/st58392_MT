import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchPageUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        # Load the search page
        self.driver.get("http://max/search")
        
        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header:
            self.fail("Header is not visible")
        
        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer:
            self.fail("Footer is not visible")
        
        # Check search form
        search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "q")))
        if not search_input:
            self.fail("Search input field is not visible")

        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-button")))
        if not search_button:
            self.fail("Search button is not clickable")
        
        # Interact with elements
        search_input.send_keys("book")
        search_button.click()
        
        # Check if products are displayed
        product_grid = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))
        if not product_grid:
            self.fail("Product grid is not visible")
        
        # Verify navigation links
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".top-menu.notmobile li a")))
        if not nav_links:
            self.fail("Navigation links are not visible")

        # Check advanced search toggle
        adv_search_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, "advs")))
        if not adv_search_checkbox:
            self.fail("Advanced search checkbox is not visible")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()