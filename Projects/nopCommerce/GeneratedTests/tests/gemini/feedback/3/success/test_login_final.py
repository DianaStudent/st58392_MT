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
        home_page_title = self.driver.title
        self.assertTrue(home_page_title is not None and home_page_title != "", "Home page title is missing or empty.")

        # 2. Click the "Log in" button in the top navigation.
        try:
            login_link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Log in' link: {e}")

        # 3. Wait until the login page loads fully.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load: {e}")

        # 4. Fill in the email and password fields using the provided credentials.
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
            self.fail(f"Could not find or fill in email/password fields: {e}")

        # 5. Click the login button.
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the login button: {e}")

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertTrue(logout_link.is_displayed(), "Log out link is not displayed, login failed.")
        except Exception as e:
            self.fail(f"Log out link not found or not visible after login: {e}")

if __name__ == "__main__":
    unittest.main()