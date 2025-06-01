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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page.
        # 2. Click on the account icon/button in the top-right.
        account_button_locator = (By.CLASS_NAME, "account-setting-active")
        try:
            account_button = self.wait.until(EC.element_to_be_clickable(account_button_locator))
            account_button.click()
        except Exception as e:
            self.fail(f"Could not find or click account button: {e}")

        # 3. Wait for the dropdown and click the "Login" link.
        login_link_locator = (By.XPATH, "//a[text()='Login']")
        try:
            login_link = self.wait.until(EC.element_to_be_clickable(login_link_locator))
            login_link.click()
        except Exception as e:
            self.fail(f"Could not find or click login link: {e}")

        # 4. Wait for the login form to appear.
        username_field_locator = (By.NAME, "username")
        try:
            self.wait.until(EC.element_to_be_clickable(username_field_locator))
        except Exception as e:
            self.fail(f"Login form did not appear: {e}")

        # 5. Fill in the username and password fields using credentials.
        username = "test2@user.com"
        password = "test**11"

        try:
            username_field = self.driver.find_element(*username_field_locator)
            username_field.send_keys(username)
            password_field = self.driver.find_element(By.NAME, "loginPassword")
            password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Could not fill in username or password: {e}")

        # 6. Click the login button.
        login_button_locator = (By.XPATH, "//button[text()='Login']")
        try:
            login_button = self.driver.find_element(*login_button_locator)
            login_button.click()
        except Exception as e:
            self.fail(f"Could not click login button: {e}")

        # 7. Wait for redirection or page update.
        # 8. Confirm successful login by verifying that the current URL contains "/my-account".
        try:
            self.wait.until(EC.url_contains("/my-account"))
            current_url = self.driver.current_url
            if "/my-account" not in current_url:
                self.fail(f"Login failed. Expected '/my-account' in URL, but got: {current_url}")
        except Exception as e:
            self.fail(f"Login failed or redirection to /my-account did not happen: {e}")

if __name__ == "__main__":
    unittest.main()