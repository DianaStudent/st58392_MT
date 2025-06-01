import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Click the account icon
        try:
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found or not clickable.")

        # Click the "Login" link
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found or not clickable.")

        # Fill in the email and password fields
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            email_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
        except:
            self.fail("Email or password field not found.")

        # Submit the login form
        try:
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )
            login_button.click()
        except:
            self.fail("Login button not found or not clickable.")

        # Confirm success by checking the URL
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Login failed. URL does not contain '/my-account'.")

if __name__ == "__main__":
    unittest.main()