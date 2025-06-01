import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    URL = "http://max/"
    EMAIL = "admin@admin.com"
    PASSWORD = "admin"

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "Login" button in the top navigation.
        try:
            my_account_link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

        # 3. Wait until the login page loads fully.
        try:
            login_page_title = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Welcome, Please Sign In!']"))
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # 4. Fill in the email and password fields using the provided credentials.
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(self.EMAIL)
        except Exception as e:
            self.fail(f"Could not find or fill email input: {e}")

        try:
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys(self.PASSWORD)
        except Exception as e:
            self.fail(f"Could not find or fill password input: {e}")

        # 5. Click the login button.
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click login button: {e}")

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertIsNotNone(logout_link, "Log out link not found after login.")
        except Exception as e:
            self.fail(f"Login failed. Could not find 'Log out' link: {e}")

if __name__ == "__main__":
    unittest.main()