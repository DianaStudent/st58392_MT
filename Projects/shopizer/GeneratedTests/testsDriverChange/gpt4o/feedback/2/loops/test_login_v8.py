import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not found: {e}")

        # Click on the account icon/button in the top-right
        try:
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon/button not clickable: {e}")

        # Wait for the dropdown and click the "Login" link
        try:
            login_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found: {e}")

        # Wait for the login form to appear
        try:
            username_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
        except Exception as e:
            self.fail(f"Username input field not found: {e}")

        # Fill in the username and password fields using credentials
        username_input.send_keys("test2@user.com")

        try:
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            password_input.send_keys("test**11")
        except Exception as e:
            self.fail(f"Password input field not found: {e}")

        # Click the login button
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'] > span"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found: {e}")

        # Wait for redirection or page update
        try:
            self.wait.until(
                EC.url_contains("/my-account")
            )
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Login was not successful or wrong redirection.")
        except Exception as e:
            self.fail(f"Redirect to '/my-account' page failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()