from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver

        # Click on the account icon
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))).click()

        # Click the Login link on the dropdown
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        self.assertIsNotNone(login_link, "Login link not present")
        login_link.click()

        # Wait for the login form to appear
        username_field = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password_field = self.wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))

        # Fill in credentials
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the Login button
        login_button = driver.find_element(By.XPATH, "//button[contains(., 'Login')]")
        self.assertIsNotNone(login_button, "Login button not present")
        login_button.click()

        # Wait for redirection to my account page
        self.wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login failed, did not find /my-account in URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()