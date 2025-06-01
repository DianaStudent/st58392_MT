import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Accept cookies if present
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookie accept button not found!")

        # Click account icon
        try:
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found!")

        # Click login link
        try:
            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found!")

        # Enter email address
        try:
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            email_input.send_keys("test2@user.com")
        except:
            self.fail("Email input not found!")

        # Enter password
        try:
            password_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
            password_input.send_keys("test**11")
        except:
            self.fail("Password input not found!")

        # Click the login button
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']"))
            )
            login_button.click()
        except:
            self.fail("Login button not found!")

        # Check for successful login
        try:
            self.wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Redirect to my-account page failed!")
        except:
            self.fail("Login was not successful!")

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()