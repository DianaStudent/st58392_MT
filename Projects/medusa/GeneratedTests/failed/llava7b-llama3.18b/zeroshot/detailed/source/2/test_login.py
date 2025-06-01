from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")

    def test_login_detailed(self):
        # Click the "Account" button
        account_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='account']"))
        )
        account_button.click()

        # Wait for login page to load
        login_page_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page-title']"))
        )

        # Enter email and password
        email_input = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        email_input.send_keys("user@test.com")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Click the sign-in button
        signin_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='signin-button']"))
        )
        signin_button.click()

        # Verify welcome message is present
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()