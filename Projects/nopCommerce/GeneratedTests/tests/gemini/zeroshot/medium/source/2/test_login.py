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
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "My account" link.
        try:
            my_account_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not click 'My account' link: {e}")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

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
            self.fail(f"Could not enter email or password: {e}")

        # 5. Click the login button to submit the form.
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not click login button: {e}")

        # 6. Verify that the user is logged in by checking the "Administration" link is present in the top navigation.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
        except Exception as e:
            self.fail(f"Login failed. Could not find 'Administration' link: {e}")

if __name__ == "__main__":
    unittest.main()