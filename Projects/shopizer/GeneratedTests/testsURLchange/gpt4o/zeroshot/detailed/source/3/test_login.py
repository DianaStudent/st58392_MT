from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome WebDriver using WebDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Wait for and click the account icon/button
        try:
            account_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            account_icon.click()
        except Exception as e:
            self.fail("Account icon not found or clickable")

        # Wait for and click the "Login" link
        try:
            login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail("Login link not found or clickable")

        # Wait for the login form to appear
        try:
            login_form = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form-container")))
        except Exception as e:
            self.fail("Login form not found or not visible")

        # Fill in the username and password fields
        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
        except Exception as e:
            self.fail("Username or password field not found")

        # Click the login button
        try:
            login_button = login_form.find_element(By.TAG_NAME, "button")
            login_button.click()
        except Exception as e:
            self.fail("Login button not found or not clickable")

        # Wait for redirection or page update and verify successful login
        try:
            self.wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail("Login failed or '/my-account' not in URL")

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()