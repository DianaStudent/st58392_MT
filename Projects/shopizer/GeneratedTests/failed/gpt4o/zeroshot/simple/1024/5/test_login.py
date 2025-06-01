from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        try:
            # Accept cookies
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()

            # Click the account icon to open account settings
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_icon.click()

            # Click the login link
            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Wait for the login form to appear
            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            # Enter credentials
            email_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
            login_button.click()

            # Confirm redirection to "/my-account"
            self.wait.until(EC.url_contains("/my-account"))

        except TimeoutException:
            self.fail("Login process failed due to a missing element or timeout.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()