import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for the page to load and ensure the "My account" link is present
        try:
            my_account_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            if not my_account_link.text.strip():
                self.fail("My account link is empty")
        except Exception:
            self.fail("My account link not found")

        my_account_link.click()

        # Wait for the login page to load
        try:
            login_form = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "form[action='/login?returnurl=%2F']"))
            )
        except Exception:
            self.fail("Login form not found")

        # Fill email and password
        try:
            email_input = driver.find_element(By.ID, "Email")
            password_input = driver.find_element(By.ID, "Password")
            
            if not email_input or not password_input:
                self.fail("Email or Password input not found")

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception:
            self.fail("Error in entering credentials")

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            if not login_button:
                self.fail("Login button not found")
            login_button.click()
        except Exception:
            self.fail("Login button click failed")

        # Verify "Log out" button is present
        try:
            logout_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            if not logout_link.text.strip():
                self.fail("Log out link is empty")
        except Exception:
            self.fail("Log out button not found, login might have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()