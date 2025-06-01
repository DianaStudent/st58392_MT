from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header elements
        try:
            # Check if logo is present
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Your store name']")))
            # Check if main navigation links are present
            nav_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
            for link_text in nav_links:
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            self.fail("Main navigation links or logo not found or not visible.")

        # Check form elements
        try:
            # Check for email input
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            # Check for password input
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            # Check for login button
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.login-button")))
        except TimeoutException:
            self.fail("Form elements (email, password, login button) not found or not visible.")
        
        # Interact with an element and check UI update
        try:
            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys("test@example.com")
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("password")
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            login_button.click()
            
            # Check if error message is displayed (assuming wrong credentials to produce error)
            wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))
        except TimeoutException:
            self.fail("Error notification not found after login attempt with wrong credentials.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()