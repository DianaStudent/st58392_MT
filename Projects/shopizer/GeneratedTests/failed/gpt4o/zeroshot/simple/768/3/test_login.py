from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the account icon
        try:
            account_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active")))
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon not found or not clickable: {e}")

        # Click the Login link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or not clickable: {e}")

        # Wait for the login form
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        except Exception as e:
            self.fail(f"Login form not visible: {e}")

        # Enter email
        try:
            email_input = driver.find_element(By.NAME, "username")
            email_input.send_keys("test2@user.com")
        except Exception as e:
            self.fail(f"Email input field not found: {e}")

        # Enter password
        try:
            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")
        except Exception as e:
            self.fail(f"Password input field not found: {e}")

        # Click the login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found: {e}")

        # Check if redirected to my-account page
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Did not redirect to account page: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()