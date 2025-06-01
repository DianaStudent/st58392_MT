from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Use the actual URL where the test should be performed.
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver

        # Click on the account icon/button in the top-right
        account_icon = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting .account-setting-active"))
        )
        self.assertTrue(account_icon)
        account_icon.click()

        # Wait for the dropdown and click the "Login" link
        login_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        self.assertTrue(login_link)
        login_link.click()

        # Wait for the login form to appear
        username_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.assertTrue(username_input)
        password_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        self.assertTrue(password_input)

        # Fill in the username and password fields using credentials
        username_input.send_keys("test2@user.com")
        password_input.send_keys("test**11")

        # Click the login button
        login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
        self.assertTrue(login_button)
        login_button.click()

        # Wait for redirection or page update
        self.wait.until(
            lambda driver: "/my-account" in driver.current_url
        )

        # Confirm successful login
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Failed to navigate to account page after login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()