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
        driver = self.driver
        credentials = {"Email": "admin@admin.com", "Password": "admin"}

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "Log in" button in the top navigation.
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Log in' link: {e}")

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

            email_input.send_keys(credentials["Email"])
            password_input.send_keys(credentials["Password"])

        except Exception as e:
            self.fail(f"Failed to find or fill email/password fields: {e}")

        # 5. Click the login button.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click the login button: {e}")

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertIsNotNone(logout_link, "Log out link is not present, login failed.")
        except Exception as e:
            self.fail(f"Failed to find 'Log out' link after login: {e}")

if __name__ == "__main__":
    unittest.main()