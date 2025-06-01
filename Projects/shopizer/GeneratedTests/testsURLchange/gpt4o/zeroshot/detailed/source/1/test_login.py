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
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click on the account icon/button in the top-right
        try:
            account_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()
        except Exception:
            self.fail("Account icon not found or could not be clicked.")

        # Wait for the dropdown and click the "Login" link
        try:
            login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception:
            self.fail("Login link not found or could not be clicked.")

        # Wait for the login form to appear
        try:
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = driver.find_element(By.NAME, "loginPassword")
        except Exception:
            self.fail("Login form not found or fields are missing.")

        # Fill in the username and password fields using credentials
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
            login_button.click()
        except Exception:
            self.fail("Login button not found or could not be clicked.")

        # Wait for redirection or page update
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception:
            self.fail("Redirection to /my-account did not occur.")

        # Confirm successful login
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login was not successful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()