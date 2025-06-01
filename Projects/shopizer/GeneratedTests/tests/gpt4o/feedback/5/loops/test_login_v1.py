from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_accept_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_accept_button.click()
        except:
            self.fail("Cookie consent button is not found.")

        # Click on account icon/button in the top-right
        try:
            account_button = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button is not found or not clickable.")

        # Wait for the login link in the dropdown
        try:
            login_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link is not found or not clickable.")

        # Wait for the login form to appear
        try:
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
        except:
            self.fail("Login form inputs are not found.")

        # Fill in the username and password fields using credentials
        username_input.send_keys("test2@user.com")
        password_input.send_keys("test**11")

        # Click the login button
        try:
            login_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[span[text()='Login']]"))
            )
            login_button.click()
        except:
            self.fail("Login button is not found or not clickable.")

        # Wait for redirection or page update, confirm successful login
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
        except:
            self.fail("Login failed or not redirected to the my-account page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()