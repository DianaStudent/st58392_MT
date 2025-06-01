import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie acceptance button could not be found - {e}")

        # Click the account icon
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()
        except Exception as e:
            self.fail(f"Account icon button could not be found - {e}")

        # Click the login link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail(f"Login link could not be found - {e}")

        # Fill in login form
        try:
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = driver.find_element(By.CLASS_NAME, "user-password")
            username_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
        except Exception as e:
            self.fail(f"Failed to find or fill login input fields - {e}")

        # Click login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            login_button.click()
        except Exception as e:
            self.fail(f"Login button could not be found - {e}")

        # Check if redirected to my-account
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Browser was not redirected to /my-account - {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()