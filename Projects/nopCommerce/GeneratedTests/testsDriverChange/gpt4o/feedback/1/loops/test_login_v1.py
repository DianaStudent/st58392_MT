import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("http://max/")

        # Wait for and click the "My account" link in top navigation to go to login page.
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
        except Exception:
            self.fail("My account link was not found on the home page.")
        
        my_account_link.click()

        # Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception:
            self.fail("Login page did not load properly.")

        # Fill in the login form.
        try:
            email_input = driver.find_element(By.ID, "Email")
            password_input = driver.find_element(By.ID, "Password")
        except Exception:
            self.fail("Email or Password input fields are missing on the login page.")
        
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click the login button.
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
        except Exception:
            self.fail("Login button is missing on the login page.")
        
        login_button.click()

        # Verify that the user is logged in.
        try:
            log_out_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            if not log_out_button.is_displayed():
                self.fail("Log out button is not displayed, indicating a failed login.")
        except Exception:
            self.fail("Log out button was not found, indicating a failed login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()