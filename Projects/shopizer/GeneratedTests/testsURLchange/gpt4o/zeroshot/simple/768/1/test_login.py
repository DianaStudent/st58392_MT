from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        try:
            # Click the cookie acceptance button
            cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_btn.click()

            # Click the account icon
            account_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()

            # Click the Login link
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()

            # Fill in the login form
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            email_input.send_keys("test2@user.com")

            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")

            # Submit the login form
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            login_button.click()

            # Confirm redirection to the "My Account" page
            wait.until(EC.url_contains("/my-account"))

        except Exception as e:
            self.fail(f"Test failed due to an unexpected exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()