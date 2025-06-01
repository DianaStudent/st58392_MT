from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestMedusaLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")
    
    def test_login(self):
        driver = self.driver
        
        # Navigate to the login page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-account-link']"))
            )
            account_link.click()
        except TimeoutException:
            self.fail("Account link not found")
        
        # Enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")
        except TimeoutException:
            self.fail("Email input field not found")
        
        # Enter password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='password-input']"))
            )
            password_input.send_keys("testuser")
        except TimeoutException:
            self.fail("Password input field not found")
        
        # Submit the login form
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='sign-in-button']"))
            )
            sign_in_button.click()
        except TimeoutException:
            self.fail("Sign in button not found or clickable")
        
        # Confirm successful login
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[@data-testid='welcome-message' and contains(text(), 'Hello user')]"))
            )
            self.assertTrue(welcome_message.is_displayed(), "Login failed: Welcome message not displayed")
        except TimeoutException:
            self.fail("Welcome message not found")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()