import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except:
            self.fail("Could not find the Accept Cookies button.")

        # Open login form
        try:
            account_icon = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_icon.click()

            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("The Login link is not available.")

        # Fill login form
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )

            email_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Failed to interact with the login form.")

        # Confirm success by checking for "/my-account" in URL
        try:
            self.wait.until(
                lambda driver: "/my-account" in driver.current_url
            )
        except:
            self.fail("Login was not successful, '/my-account' not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()