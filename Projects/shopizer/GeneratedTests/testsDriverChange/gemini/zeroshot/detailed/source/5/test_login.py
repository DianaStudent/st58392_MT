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
        self.email = "test2@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Click on the account icon
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        # Click on the Login link
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        # Wait for the login form to appear
        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
        except:
            self.fail("Username field not found")

        # Fill in the username and password
        username_field.send_keys(self.email)
        password_field = driver.find_element(By.NAME, "loginPassword")
        password_field.send_keys(self.password)

        # Click the login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
            )
            login_button.click()
        except:
            self.fail("Login button not found")

        # Wait for redirection and confirm successful login
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Login failed or redirection to /my-account did not occur")

if __name__ == "__main__":
    unittest.main()