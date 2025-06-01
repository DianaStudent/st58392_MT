import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080")  # Update with the actual URL

    def test_login(self):
        driver = self.driver

        # Accept cookies if the consent is presented
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not found or clickable: {str(e)}")
        
        # Click the account icon to open dropdown
        try:
            account_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon not found or clickable: {str(e)}")

        # Click the login link from dropdown
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or clickable: {str(e)}")

        # Enter the login details
        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys("test2@user.com")

            password_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
            password_field.send_keys("test**11")

            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'] > span"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Login form elements not found or clickable: {str(e)}")

        # Check if redirected to /my-account
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
        except Exception as e:
            self.fail(f"Redirection to /my-account not successful: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()