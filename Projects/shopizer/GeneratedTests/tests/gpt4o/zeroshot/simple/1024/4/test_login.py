import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        
        try:
            # Accept cookies
            accept_cookies_btn = self.wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()

            # Click on the account icon to open the dropdown
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_icon.click()
            
            # Click on the Login link in the dropdown
            login_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Enter login credentials
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
            
            # Submit the login form
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']"))
            )
            login_button.click()
            
            # Verify successful login by checking the URL
            self.wait.until(
                EC.url_contains("/my-account")
            )
            
        except TimeoutException as e:
            self.fail(f"Test failed due to timeout: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()