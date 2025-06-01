import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITestCase(unittest.TestCase):
    def setUp(self):
        """Set up Chrome WebDriver."""
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        """Test to confirm UI elements and interactions."""
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the page
        driver.get("http://example.com")  # Replace with the actual URL
        
        # Step 2: Confirm the presence of key interface elements
        try:
            # Header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header)
            
            # Navigation links
            nav_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav ul.nav-level-0")))
            self.assertIsNotNone(nav_links)
            
            # Search input
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box .search-input")))
            self.assertIsNotNone(search_input)
            
            # Banner in the home slider
            home_slider = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".home-slider")))
            self.assertIsNotNone(home_slider)
            
            # Products section with product names and prices
            products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products .available")))
            self.assertIsNotNone(products)
            
        except Exception as e:
            self.fail(f"Key interface element not found or visible: {str(e)}")
        
        # Step 3: Interact with one or two elements
        try:
            # Click on a navigation link to 'Category A'
            category_a_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
            category_a_link.click()
            
            # Verify UI updates by checking the presence of Subcategory navigation
            subcategory_navigation = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.nav-level-1")))
            self.assertIsNotNone(subcategory_navigation)
            
        except Exception as e:
            self.fail(f"Failed to interact with elements or UI did not update as expected: {str(e)}")

        # Step 4: Verify interactive elements do not cause errors in the UI
        try:
            # Interacting with search button to confirm no errors
            search_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-icon-search")))
            search_icon.click()
            
            # Ensure no error message appears
            error_message = driver.find_elements(By.CSS_SELECTOR, ".error-message")
            self.assertFalse(error_message, "Found unexpected error message elements in UI")
        
        except Exception as e:
            self.fail(f"UI interaction caused errors: {str(e)}")
    
    def tearDown(self):
        """Close the browser."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()