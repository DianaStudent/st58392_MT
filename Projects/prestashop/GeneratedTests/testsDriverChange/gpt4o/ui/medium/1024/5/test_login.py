import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check navigation links are present
        nav_links = [
            ('Home', 'http://localhost:8080/en/'),
            ('Clothes', 'http://localhost:8080/en/3-clothes'),
            ('Accessories', 'http://localhost:8080/en/6-accessories'),
            ('Art', 'http://localhost:8080/en/9-art')
        ]
        
        for link_text, href in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertEqual(link.get_attribute("href"), href, f"Link '{link_text}' not correct.")
        
        # Check login form elements
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))

        self.assertTrue(email_input.is_displayed(), "Email input not visible.")
        self.assertTrue(password_input.is_displayed(), "Password input not visible.")
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button not visible.")
        
        # Interact with sign in button
        email_input.send_keys("test@example.com")
        password_input.send_keys("Password123")
        sign_in_button.click()

        # Check if Forgot Password link is visible
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot password link not visible.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()