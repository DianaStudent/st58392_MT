from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        # Accept cookies if button is present
        try:
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except:
            print("No cookies button or already accepted.")

        # Click on the account setting icon to show the dropdown
        try:
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account setting icon not found.")

        # Click on the Login link
        try:
            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found.")

        # Enter login details
        try:
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")

            # Click on login button
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']/span[text()='Login']"))
            )
            login_button.click()
        except:
            self.fail("Login form elements not found or login button not clickable.")

        # Verify that URL contains '/my-account'
        try:
            self.wait.until(
                EC.url_contains("/my-account")
            )
        except:
            self.fail("Login failed or not redirected to '/my-account'.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()