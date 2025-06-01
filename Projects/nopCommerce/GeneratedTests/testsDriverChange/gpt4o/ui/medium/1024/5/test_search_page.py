import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check for navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
        except:
            self.fail("Home page link not found or not visible.")
        
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        except:
            self.fail("Search input field not found or not visible.")
        
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        except:
            self.fail("Search button not found or not visible.")

        # Interact with the search button
        search_input.clear()
        search_input.send_keys("book")
        search_button.click()
        
        # Verify no errors occur
        try:
            search_results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))
        except:
            self.fail("Search results not displayed or error occurred.")
    
    def tearDown(self):
        # Tear down the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()