from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the account icon/button in the top-right
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active"))
        )
        if not account_button:
            self.fail("Account button is missing")
        account_button.click()

        # Step 2: Wait for the dropdown and click the "Login" link
        login_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        if not login_link:
            self.fail("Login link is missing")
        login_link.click()

        # Step 3: Wait for the login form to appear
        username_input = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )

        if not username_input or not password_input:
            self.fail("Username or password field is missing")

        # Step 4: Fill in the username and password fields
        username_input.send_keys("test2@user.com")
        password_input.send_keys("test**11")

        # Step 5: Click the login button
        login_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )
        if not login_button:
            self.fail("Login button is missing")
        login_button.click()

        # Step 6: Wait for redirection or page update
        wait.until(EC.url_contains("/my-account"))

        # Step 7: Confirm successful login by verifying the URL
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login failed or not redirected to /my-account")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()