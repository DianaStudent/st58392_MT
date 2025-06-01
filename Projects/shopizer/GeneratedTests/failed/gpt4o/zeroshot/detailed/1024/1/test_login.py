from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_accept_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_accept_button.click()
        except Exception:
            self.fail("Cookie accept button not found or clickable")

        # Click on account icon/button
        try:
            account_icon = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except Exception:
            self.fail("Account icon/button not found or clickable")

        # Click on the "Login" link
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception:
            self.fail("Login link not found or clickable")

        # Wait for the login form to appear
        try:
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']/span[text()='Login']"))
            )
        except Exception:
            self.fail("Login form elements not found")

        # Fill in the username and password
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the login button
        login_button.click()

        # Wait for redirection or page update
        try:
            wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "URL does not contain '/my-account'")
        except Exception:
            self.fail("Redirection to /my-account failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()