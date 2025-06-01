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
        email = "admin@admin.com"
        password = "admin"

        # 1. Open the home page. (Done in setUp)

        # 2. Click the "My account" button in the top navigation.
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

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
            email_input.send_keys(email)
            password_input.send_keys(password)
        except Exception as e:
            self.fail(f"Could not find or fill email/password fields: {e}")

        # 5. Click the login button.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click login button: {e}")

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertIsNotNone(logout_link)

        except Exception as e:
            self.fail(f"Login failed. Could not find 'Log out' link: {e}")

if __name__ == "__main__":
    unittest.main()