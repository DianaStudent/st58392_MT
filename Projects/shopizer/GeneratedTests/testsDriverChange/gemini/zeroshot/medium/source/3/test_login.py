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
        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Click account icon
        try:
            account_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Could not find or click the account icon.")

        # Click login link
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Could not find or click the login link.")

        # Fill in the login form
        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            username_field.send_keys("test2@user.com")
            password_field.send_keys("test**11")
        except:
            self.fail("Could not find username or password field.")

        # Submit the form
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )
            login_button.click()
        except:
            self.fail("Could not find or click the login button.")

        # Verify successful login by checking the URL
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Login failed. URL does not contain '/my-account'.")

if __name__ == "__main__":
    unittest.main()