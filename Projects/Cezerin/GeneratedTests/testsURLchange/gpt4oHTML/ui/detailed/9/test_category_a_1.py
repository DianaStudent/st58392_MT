import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8," + html_data['html'])
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # 1. Ensure structural elements (e.g., header, footer, navigation) are visible
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))

        # 2. Check presence and visibility of input fields, buttons, labels, and sections
        search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        sort_select = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'select')))
        filter_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'button.is-fullwidth')))
        
        # 3. Interact with key UI elements
        filter_button.click()
        
        # Confirm the interaction by checking some expected change or output
        # For example, let's check if a close button appears after clicking filter
        close_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'is-dark')))
        
        # 4. Confirm that the UI reacts visually (assert interaction result)
        self.assertTrue(close_button.is_displayed(), "Close button after filter interaction is not displayed")
        
        # 5. Assert that no required UI element is missing
        if not all([header, footer, navigation, search_input, sort_select, filter_button, close_button]):
            self.fail("One or more required UI elements are missing.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)