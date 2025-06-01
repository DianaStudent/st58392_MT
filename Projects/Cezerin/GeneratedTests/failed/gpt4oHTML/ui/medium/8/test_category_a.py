from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA(unittest.TestCase):
    
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://example.com/category-a')  # Use the actual domain here

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for the presence of navigation links
        try:
            nav_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.nav-level-0')))
        except:
            self.fail("Navigation links not present or not visible.")
        
        # Check for the presence of form fields
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            self.assertEqual(search_input.get_attribute('placeholder'), 'Search')
        except:
            self.fail("Search input not present or not visible.")
        
        # Check for the presence of buttons
        try:
            sort_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort-title')))
            filter_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.is-fullwidth')))
        except:
            self.fail("Either sort or filter button not present or not visible.")
        
        # Check for a banner or hero section
        try:
            hero_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section.hero')))
        except:
            self.fail("Hero section not present or not visible.")

    def test_ui_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Interact with a search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            search_input.clear()
            search_input.send_keys('Product A')
        except:
            self.fail("Unable to interact with the search input.")
        
        # Interact with the sort functionality
        try:
            sort_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select')))
            sort_select.click()
            sort_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'option[value="price"]')))
            sort_option.click()
        except:
            self.fail("Unable to interact with the sort functionality.")
        
        # Ensure no UI errors appear after interaction
        try:
            driver.find_elements(By.CSS_SELECTOR, 'div.error')  # Adjust selector if specific error classes are known
            self.assertFalse(driver.find_elements(By.CSS_SELECTOR, 'div.error'), "UI error detected after interaction.")
        except:
            self.fail("Error checking failed or UI error detected.")

if __name__ == "__main__":
    unittest.main()