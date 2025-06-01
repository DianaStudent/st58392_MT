from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Wait for and click the account icon/button
        account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_icon.click()

        # Wait for and click the "Login" link in the dropdown
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Wait for login form to appear
        username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        if not username_field:
            self.fail("Username input field not found.")

        password_field = wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
        if not password_field:
            self.fail("Password input field not found.")
        
        # Fill in credentials
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        if not login_button:
            self.fail("Login button not found.")
        login_button.click()

        # Wait for page to update and verify successful login by checking URL
        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login failed or user not redirected to account page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()