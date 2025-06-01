from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Click the account icon
        try:
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon not found or not clickable: {e}")

        # Click the "Login" link
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or not clickable: {e}")

        # Fill in the email and password fields
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            email_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
        except Exception as e:
            self.fail(f"Email or password field not found: {e}")

        # Submit the login form
        try:
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or not clickable: {e}")

        # Confirm success by checking the URL
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Login failed or redirect to /my-account did not occur: {e}")

if __name__ == "__main__":
    unittest.main()