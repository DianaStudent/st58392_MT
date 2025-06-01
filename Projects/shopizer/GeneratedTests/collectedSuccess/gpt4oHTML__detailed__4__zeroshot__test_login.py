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
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get("http://localhost/")

        # Step 2: Click on the account icon/button in the top-right
        try:
            account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            account_icon.click()
        except Exception:
            self.fail("Account icon/button not found or not clickable")

        # Step 3: Wait for the dropdown and click the "Login" link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/login']")))
            login_link.click()
        except Exception:
            self.fail("Login link not found or not clickable")

        # Step 4: Wait for the login form to appear
        try:
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        except Exception:
            self.fail("Login form with username field not found")

        # Step 5: Fill in the username and password fields using credentials
        username_field.send_keys("test2@user.com")
        
        try:
            password_field = driver.find_element(By.NAME, "loginPassword")
        except Exception:
            self.fail("Password field not found")
        
        password_field.send_keys("test**11")

        # Step 6: Click the login button
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button-box button[type='submit']")))
            login_button.click()
        except Exception:
            self.fail("Login button not found or not clickable")

        # Step 7: Wait for redirection or page update
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception:
            self.fail("Redirection to /my-account did not occur")

        # Step 8: Confirm successful login by verifying that the current URL contains "/my-account"
        current_url = driver.current_url
        if "/my-account" not in current_url:
            self.fail("Login failed or did not navigate to my-account page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()