import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        try:
            # Wait and click the account icon/button
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active"))
            )
            account_button.click()

            # Wait and click the "Login" link
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Wait for the login form to appear
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-form-container"))
            )
            
            # Fill in the username and password fields
            username_field = driver.find_element(By.NAME, "username")
            password_field = driver.find_element(By.NAME, "loginPassword")
            if not username_field or not password_field:
                self.fail("Username or password field is missing.")
                
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")

            # Click the login button
            login_button = driver.find_element(By.CSS_SELECTOR, "div.button-box button[type='submit']")
            if not login_button:
                self.fail("Login button is missing.")
            
            login_button.click()

            # Wait for redirection or page update
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )

            # Confirm successful login
            self.assertIn("/my-account", driver.current_url, "Login was not successful.")

        except Exception as e:
            self.fail(f"Test encountered an error: {e}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()