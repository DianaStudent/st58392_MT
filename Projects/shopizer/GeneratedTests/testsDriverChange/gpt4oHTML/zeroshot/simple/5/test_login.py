import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Click the account icon.
        try:
            account_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_icon.click()
        except Exception as e:
            self.fail(f"Failed to find or click the account icon: {str(e)}")
        
        # Click the "Login" link.
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click the 'Login' link: {str(e)}")
        
        # Enter email.
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            email_input.send_keys("test2@user.com")
        except Exception as e:
            self.fail(f"Failed to find or fill the email input field: {str(e)}")
        
        # Enter password.
        try:
            password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            password_input.send_keys("test**11")
        except Exception as e:
            self.fail(f"Failed to find or fill the password input field: {str(e)}")
        
        # Click Login.
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']")))
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click the login button: {str(e)}")
        
        # Confirm that the user is redirected to the "my-account" page.
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Failed to verify URL contains '/my-account': {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()