import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Setup WebDriver using ChromeDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        driver.get("http://localhost:8080")  # Assume this is the base URL for your test environment

        # Click the account icon/button in the top-right
        account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .account-setting-active")))
        account_icon.click()

        # Wait for the dropdown and click the "Login" link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # Wait for the login form to appear
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
        
        # Check the existence and non-emptiness of login fields
        self.assertIsNotNone(username_input, "Username input not found.")
        self.assertIsNotNone(password_input, "Password input not found.")

        # Fill in the username and password fields using credentials
        username_input.send_keys("test2@user.com")
        password_input.send_keys("test**11")

        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        self.assertIsNotNone(login_button, "Login button not found.")
        login_button.click()

        # Wait for redirection or page update
        wait.until(EC.url_contains("/my-account"))

        # Confirm successful login by verifying that the current URL contains "/my-account"
        self.assertIn("/my-account", driver.current_url, "Login was not successful.")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()