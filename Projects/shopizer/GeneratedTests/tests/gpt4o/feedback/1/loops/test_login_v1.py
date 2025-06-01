import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found.")

        # Click account icon in the top-right
        try:
            account_icon = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found.")

        # Click "Login" link in dropdown
        try:
            login_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found.")

        # Wait for the login form to appear
        try:
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
        except:
            self.fail("Login form did not appear.")

        # Fill in credentials
        try:
            username_input.send_keys("test2@user.com")
            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")
        except:
            self.fail("Failed to fill in the login form.")

        # Click the login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
            login_button.click()
        except:
            self.fail("Login button not found.")

        # Wait for redirection and check current URL
        try:
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "user-profile"))
            )
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Login failed, '/my-account' not in URL.")
        except:
            self.fail("Redirection to /my-account failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()