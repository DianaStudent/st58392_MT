from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver
        
        # Step 1: Accept Cookies
        try:
            accept_cookies = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except Exception as e:
            self.fail(f"Cookies consent button missing: {e}")
        
        # Step 2: Click the account icon in the top navigation bar
        try:
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon missing: {e}")
        
        # Step 3: Click the "Login" link
        try:
            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link missing: {e}")
        
        # Step 4: Fill in the email and password fields
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
        except Exception as e:
            self.fail(f"Login form elements missing: {e}")

        email_input.send_keys("test2@user.com")
        password_input.send_keys("test**11")
        
        # Step 5: Submit the login form
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Login button missing or not clickable: {e}")
        
        # Step 6: Confirm success by checking the URL
        try:
            self.wait.until(lambda driver: "/my-account" in driver.current_url)
        except Exception as e:
            self.fail(f"Login failed or redirect to '/my-account' missing: {e}")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()