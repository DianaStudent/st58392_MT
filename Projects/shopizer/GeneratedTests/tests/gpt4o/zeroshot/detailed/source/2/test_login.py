import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on the account icon/button in the top-right
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'account-setting-active'))
        )
        self.assertIsNotNone(account_button, "Account button is not present")
        account_button.click()

        # Wait for the dropdown and click the "Login" link
        login_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Login'))
        )
        self.assertIsNotNone(login_link, "Login link is not present")
        login_link.click()

        # Wait for the login form to appear
        username_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        self.assertIsNotNone(username_field, "Username field is not present")

        # Fill in the username and password fields
        password_field = driver.find_element(By.NAME, 'loginPassword')
        self.assertIsNotNone(password_field, "Password field is not present")

        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, '.button-box button[type="submit"]')
        self.assertIsNotNone(login_button, "Login button is not present")
        login_button.click()

        # Wait for redirection or page update
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'user-profile'))
        )

        # Confirm successful login
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login was not successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()