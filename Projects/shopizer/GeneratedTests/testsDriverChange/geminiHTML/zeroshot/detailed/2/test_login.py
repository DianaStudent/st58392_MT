import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.set_window_size(1200, 800)
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

        # 1. Open the home page - Done in setUp

        # 2. Click on the account icon/button in the top-right.
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Wait for the dropdown and click the "Login" link.
        login_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
        )
        login_link.click()

        # 4. Wait for the login form to appear.
        username_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # 5. Fill in the username and password fields.
        username_field.send_keys("test2@user.com")
        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        password_field.send_keys("test**11")

        # 6. Click the login button.
        login_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
        )
        login_button.click()

        # 7. Wait for redirection or page update.
        # 8. Confirm successful login by verifying the URL.
        self.wait.until(EC.url_contains("/my-account"))
        current_url = self.driver.current_url
        self.assertIn("/my-account", current_url, "Login failed. URL does not contain '/my-account'.")

if __name__ == "__main__":
    unittest.main()