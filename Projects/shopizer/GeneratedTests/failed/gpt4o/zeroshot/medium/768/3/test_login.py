from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except Exception as e:
            self.fail("Cookies accept button not found or clickable.")

        # Click on the account icon and login link
        try:
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except Exception as e:
            self.fail("Account icon/button not found or clickable.")

        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail("Login link not found or clickable.")

        # Enter login credentials
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            
            if email_field is None or password_field is None:
                self.fail("Email or password fields are missing.")

            email_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
        except Exception as e:
            self.fail(f"Error while entering login credentials: {str(e)}")

        # Submit the login form
        try:
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span='Login']"))
            )
            login_button.click()
        except Exception as e:
            self.fail("Login button not found or clickable.")

        # Confirm success by checking redirection
        try:
            wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)
        except Exception as e:
            self.fail("Redirection to '/my-account' failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()