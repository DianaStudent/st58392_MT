import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.email = "admin@admin.com"
        self.password = "admin"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 2. Click the "Log in" button in the top navigation.
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
            )
            if login_link:
                login_link.click()
            else:
                self.fail("Log in link not found.")
        except Exception as e:
            self.fail(f"Failed to click 'Log in' link: {e}")

        # 3. Wait until the login page loads fully.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # 4. Fill in the email and password fields using the provided credentials.
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )

            if email_input and password_input:
                email_input.send_keys(self.email)
                password_input.send_keys(self.password)
            else:
                self.fail("Email or Password input field not found.")

        except Exception as e:
            self.fail(f"Failed to fill in email or password: {e}")

        # 5. Click the login button.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
            )
            if login_button:
                login_button.click()
            else:
                self.fail("Login button not found.")
        except Exception as e:
            self.fail(f"Failed to click the login button: {e}")

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )

            if logout_link:
                self.assertIsNotNone(logout_link, "Log out link is not present after login.")
            else:
                self.fail("Log out link not found after login.")

        except Exception as e:
            self.fail(f"Login verification failed: {e}")

if __name__ == "__main__":
    unittest.main()