from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):
    def setUp(self):
        # Setup WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
    
    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check presence of the header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is not present.")

        # Check for navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".primary-nav a")
        self.assertGreaterEqual(len(nav_links), 1, "Navigation links are not present.")
        
        # Check that category titles are present
        category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
        self.assertIsNotNone(category_title, "Category title is not present.")

        # Check for product elements
        products = driver.find_elements(By.CSS_SELECTOR, ".products .product-name")
        self.assertGreaterEqual(len(products), 1, "Products are not listed.")

        # Check presence of search input
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        self.assertIsNotNone(search_input, "Search input is not visible.")
        
        # Check presence of buttons
        sort_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select")))
        self.assertIsNotNone(sort_button, "Sort button is not present.")
    
    def test_interactive_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click on the search button and ensure no error
        search_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-icon-search")))
        search_icon.click()

        # Verify no visible errors after interaction
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".error-message")
            self.fail("Error message displayed: " + error_message.text)
        except:
            pass

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()