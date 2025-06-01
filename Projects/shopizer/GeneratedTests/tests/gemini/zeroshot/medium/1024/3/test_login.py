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
        email = "test2@user.com"
        password = "test**11"

        try:
            # Accept cookies
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Click the account icon
        account_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
        )
        account_icon.click()

        # Click the "Login" link
        login_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
        )
        login_link.click()

        # Fill in the email and password fields
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.assertIsNotNone(username_field, "Username field not found")
        username_field.send_keys(email)

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        self.assertIsNotNone(password_field, "Password field not found")
        password_field.send_keys(password)

        # Submit the login form
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span='Login']"))
        )
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()

        # Confirm success by checking that the URL contains "/my-account"
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Login failed. URL does not contain /my-account")

if __name__ == "__main__":
    unittest.main()