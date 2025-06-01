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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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

        # Click on the account icon
        try:
            account_button = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found or not clickable: {e}")

        # Click on the "Login" link
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or not clickable: {e}")

        # Wait for the login form to appear
        try:
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
        except Exception as e:
            self.fail(f"Username field not found: {e}")

        # Fill in the username and password fields
        username_field.send_keys("test2@user.com")
        try:
            password_field = driver.find_element(By.NAME, "loginPassword")
        except Exception as e:
            self.fail(f"Password field not found: {e}")
        password_field.send_keys("test**11")

        # Click the login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
            login_button.click()
        except Exception as e:
            self.fail(f"Login button not found or not clickable: {e}")

        # Wait for redirection or page update and confirm successful login
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Login failed or incorrect redirection: {e}")


if __name__ == "__main__":
    unittest.main()