from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):
    
    def setUp(self):
        # Initialize Chrome browser
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Check for the presence and visibility of key UI elements
        
        # Header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible.")
        except Exception as e:
            self.fail(f"Header check failed: {str(e)}")
        
        # Navigation links
        try:
            category_a_link = driver.find_element(By.XPATH, "//a[@href='/category-a']")
            self.assertTrue(category_a_link.is_displayed(), "Category A link is not visible.")
            category_b_link = driver.find_element(By.XPATH, "//a[@href='/category-b']")
            self.assertTrue(category_b_link.is_displayed(), "Category B link is not visible.")
        except Exception as e:
            self.fail(f"Navigation links check failed: {str(e)}")
        
        # Search box
        try:
            search_input = driver.find_element(By.CLASS_NAME, 'search-input')
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
        except Exception as e:
            self.fail(f"Search input check failed: {str(e)}")
        
        # Sort dropdown
        try:
            sort_dropdown = driver.find_element(By.TAG_NAME, 'select')
            self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible.")
        except Exception as e:
            self.fail(f"Sort dropdown check failed: {str(e)}")
        
        # Filter button on mobile
        try:
            filter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Filter products')]")
            self.assertTrue(filter_button.is_displayed(), "Filter products button is not visible.")
        except Exception as e:
            self.fail(f"Filter button check failed: {str(e)}")
        
        # Interaction: Click on Category B and check URL update
        try:
            category_b_link.click()
            self.wait.until(EC.url_contains("/category-b"))
            self.assertIn("category-b", driver.current_url, "URL did not update to Category B.")
        except Exception as e:
            self.fail(f"Interaction with Category B link failed: {str(e)}")
                   
    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()