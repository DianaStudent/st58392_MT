import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver

        # Click the "Login" link
        try:
            login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or could not be clicked: {str(e)}")
        
        # Wait for the login page to load and enter email
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
            if not email_input:
                self.fail("Email input not found or is empty.")
            email_input.send_keys("admin@admin.com")
        except Exception as e:
            self.fail(f"Email input not found or could not interact: {str(e)}")

        # Enter password
        try:
            password_input = driver.find_element(By.ID, "Password")
            if not password_input:
                self.fail("Password input not found or is empty.")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Password input not found or could not interact: {str(e)}")

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            if not login_button:
                self.fail("Login button not found or is empty.")
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or could not be clicked: {str(e)}")

        # Verify login by checking the "Log out" button
        try:
            logout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            if not logout_button:
                self.fail("Log out button not found or is empty.")
        except Exception as e:
            self.fail(f"Log out button not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()