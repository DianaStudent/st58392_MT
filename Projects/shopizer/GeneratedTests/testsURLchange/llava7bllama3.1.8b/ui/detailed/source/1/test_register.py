import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_page_structure(self):
        # Wait for the header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header')))

        # Check that the main UI components are present:
        # Header
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'h1')), 0)
        
        # Footer
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'footer')), 0)
        
        # Navigation links
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, '#navbarSupportedContent li a')
        self.assertGreaterEqual(len(nav_links), 3)

    def test_input_fields_buttons_labels(self):
        # Wait for the form to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'loginForm')))

        # Check that all required elements are present:
        login_form = self.driver.find_elements(By.ID, 'loginForm')
        
        # Username input field
        username_input = self.driver.find_element(By.NAME, 'username')
        self.assertIsNotNone(username_input)
        
        # Password input field
        password_input = self.driver.find_element(By.NAME, 'password')
        self.assertIsNotNone(password_input)
        
        # Login button
        login_button = self.driver.find_element(By.ID, 'login-button')
        self.assertIsNotNone(login_button)

    def test_interaction(self):
        # Wait for the form to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'loginForm')))

        # Click the login button
        login_button = self.driver.find_element(By.ID, 'login-button')
        login_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()