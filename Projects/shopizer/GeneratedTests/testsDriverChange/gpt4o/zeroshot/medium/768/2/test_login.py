import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def wait_for_element(self, by, value, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            self.fail(f"Element with {by}={value} not found within {timeout} seconds.")
        return None

    def test_login(self):
        driver = self.driver

        # Accept cookies if the button exists
        try:
            accept_cookies_button = self.wait_for_element(By.ID, "rcc-confirm-button")
            if accept_cookies_button and accept_cookies_button.is_displayed():
                accept_cookies_button.click()
        except NoSuchElementException:
            pass

        # Click the account icon
        account_icon = self.wait_for_element(By.CSS_SELECTOR, ".account-setting .account-setting-active")
        account_icon.click()

        # Click the "Login" link
        login_link = self.wait_for_element(By.LINK_TEXT, "Login")
        login_link.click()

        # Fill in the email field
        email_field = self.wait_for_element(By.NAME, "username")
        email_field.send_keys("test2@user.com")

        # Fill in the password field
        password_field = self.wait_for_element(By.NAME, "loginPassword")
        password_field.send_keys("test**11")

        # Click the login button
        login_button = self.wait_for_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Confirm redirection to /my-account page
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertTrue(driver.current_url.endswith("/my-account"))
        except TimeoutException:
            self.fail("Redirection to '/my-account' failed.")

if __name__ == "__main__":
    unittest.main()