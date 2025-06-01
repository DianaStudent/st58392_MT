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
        self.driver.maximize_window()
        self.driver.get("http://localhost/")  # Replace with your application URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver
        wait = self.wait

        try:
            # Accept cookies if the button is present
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if cookie_button:
                cookie_button.click()

            # Click the account icon
            account_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            if not account_icon:
                self.fail('Account icon not found.')
            account_icon.click()

            # Click the "Login" link
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            if not login_link:
                self.fail('Login link not found.')
            login_link.click()

            # Fill in the login form
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            
            if email_input and password_input:
                email_input.send_keys("test2@user.com")
                password_input.send_keys("test**11")
            else:
                self.fail('Email or password input field not found.')

            # Submit the login form
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']")))
            if not login_button:
                self.fail('Login button not found.')
            login_button.click()

            # Confirm success by checking the URL
            url_contains_my_account = wait.until(EC.url_contains("/my-account"))
            self.assertTrue(url_contains_my_account, "URL does not contain '/my-account'.")

        finally:
            # Ensure browser quits even if test fails
            driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()