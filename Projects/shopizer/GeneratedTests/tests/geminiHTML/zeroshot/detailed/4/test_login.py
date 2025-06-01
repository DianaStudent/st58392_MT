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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Accept cookies
        try:
            cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # 1. Click on the account icon/button in the top-right.
        try:
            account_button = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        # 2. Wait for the dropdown and click the "Login" link.
        try:
            login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found in dropdown")

        # 3. Wait for the login form to appear.
        try:
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
        except:
            self.fail("Login form not found")

        # 4. Fill in the username and password fields.
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # 5. Click the login button.
        try:
            login_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
            )
            login_button.click()
        except:
            self.fail("Login button not found")

        # 6. Wait for redirection or page update and confirm successful login.
        try:
            self.wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", self.driver.current_url)
        except:
            self.fail("Login failed or redirection to /my-account did not occur")

if __name__ == "__main__":
    unittest.main()