import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://localhost/")

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button is missing or not clickable.")

        # Click the account icon
        try:
            account_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()
        except:
            self.fail("Account icon is missing or not clickable.")

        # Click the 'Login' link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except:
            self.fail("'Login' link is missing or not clickable.")

        # Fill in the email and password fields
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            email_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
        except:
            self.fail("Login fields are missing or not interactable.")

        # Submit the login form
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            login_button.click()
        except:
            self.fail("Login button is missing or not clickable.")

        # Confirm success by checking that the URL contains "/my-account"
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Login was not successful or '/my-account' not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()