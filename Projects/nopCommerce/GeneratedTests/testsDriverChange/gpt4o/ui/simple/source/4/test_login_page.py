import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome webdriver
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        # Check the page title
        self.assertIn("Your store. Login", self.driver.title)

        # Check presence of key UI elements

        # Header elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-upper')))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-logo')))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box')))

        # Menu links
        menu_links = ['Home page', 'New products', 'Search', 'My account', 'Blog', 'Contact us']
        for link_text in menu_links:
            menu_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(menu_link.is_displayed(), f"Menu link '{link_text}' is not visible")
        
        # Login form elements
        self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
        login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        
        # Register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")
        
        # Check footer elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-upper')))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'social')))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'newsletter')))

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()