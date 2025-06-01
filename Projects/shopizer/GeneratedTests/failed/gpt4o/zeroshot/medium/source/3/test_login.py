from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except TimeoutException:
            self.fail("Cookie accept button is not found or clickable")
        
        # Click the account icon
        try:
            account_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_icon.click()
        except TimeoutException:
            self.fail("Account icon is not found or clickable")
        
        # Click the login link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except TimeoutException:
            self.fail("Login link is not found or clickable")
        
        # Fill in email and password fields
        try:
            email_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            email_field.send_keys("test2@user.com")
            
            password_field = wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
            password_field.send_keys("test**11")
        except TimeoutException:
            self.fail("Email or password field is not found")
        
        # Submit the login form
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            login_button.click()
        except TimeoutException:
            self.fail("Login button is not found or clickable")
        
        # Confirm success by checking that the URL contains "/my-account"
        try:
            wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Login was not successful, '/my-account' not in URL")
        except TimeoutException:
            self.fail("Failed to redirect to the '/my-account' page")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()