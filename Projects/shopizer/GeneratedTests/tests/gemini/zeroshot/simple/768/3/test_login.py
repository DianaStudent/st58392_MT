import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.email = "test2@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Click account icon
        try:
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found or not clickable")

        # Click Login link
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found or not clickable")

        # Fill in login form
        try:
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            username_field.send_keys(self.email)
            password_field.send_keys(self.password)
        except:
            self.fail("Username or password field not found")

        # Click Login button
        try:
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
            )
            login_button.click()
        except:
            self.fail("Login button not found or not clickable")

        # Check for successful login
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertTrue("/my-account" in driver.current_url)
        except:
            self.fail("Login failed or redirect to /my-account did not occur")

if __name__ == "__main__":
    unittest.main()