from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        try:
            # Accept cookies
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()

            # Click account icon
            account_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()

            # Click the "Login" link
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            if login_link.is_displayed():
                login_link.click()
            else:
                self.fail("Login link not found or not displayed.")

            # Fill in the email and password fields
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            password_input = wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))

            if email_input.is_displayed() and password_input.is_displayed():
                email_input.send_keys("test2@user.com")
                password_input.send_keys("test**11")
            else:
                self.fail("Email or password input fields not found or not displayed.")

            # Submit the login form
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']")))
            login_button.click()

            # Confirm success by checking "/my-account" in the URL
            wait.until(EC.url_contains("/my-account"))

        except Exception as e:
            self.fail(f"Test failed with exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()