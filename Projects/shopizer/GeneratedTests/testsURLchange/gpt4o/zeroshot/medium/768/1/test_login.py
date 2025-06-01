import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Wait for the account icon and click it
        account_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_icon.click()

        # Wait for the login link and click it
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # Wait for the email field, check it exists and is not empty
        email_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        if not email_field:
            self.fail("Email input not found or is empty")

        # Enter the email
        email_field.send_keys("test2@user.com")

        # Check the password field exists and is not empty
        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        if not password_field:
            self.fail("Password input not found or is empty")

        # Enter the password
        password_field.send_keys("test**11")

        # Submit the login form
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']"))
        )
        submit_button.click()

        # Assert URL contains "/my-account"
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()