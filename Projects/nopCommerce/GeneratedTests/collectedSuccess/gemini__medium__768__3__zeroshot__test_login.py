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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page. (Already done in setUp)

        # 2. Click the "Login" link.
        try:
            login_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or not clickable: {e}")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load: {e}")

        # 4. Enter the email and password.
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")

        except Exception as e:
            self.fail(f"Email or password input not found: {e}")

        # 5. Click the login button to submit the form.
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or not clickable: {e}")

        # 6. Verify that the user is logged in by checking the "Administration" link is present.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
        except:
            self.fail("Login failed: Administration link not found after login.")

if __name__ == "__main__":
    unittest.main()