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
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except Exception:
            self.fail("Cookie consent button not found")

        # Open the login form
        try:
            account_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()

            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception:
            self.fail("Login link not found")

        # Fill login form
        try:
            username_field = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            username_field.send_keys("test2@user.com")

            password_field = driver.find_element(By.CLASS_NAME, "user-password")
            password_field.send_keys("test**11")

            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            login_button.click()
        except Exception:
            self.fail("Login form elements not found")

        # Verify login by checking redirection to my-account page
        try:
            self.wait.until(EC.url_contains("/my-account"))
        except Exception:
            self.fail("Login failed or not redirected to my-account page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()