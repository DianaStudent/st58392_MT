import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Click on the account icon
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        # Click the "Login" link
        login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
        login_link.click()

        # Wait for the login form to appear
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))

        # Fill in the username and password fields
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Click the login button
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Login')]")))
        login_button.click()

        # Wait for redirection or page update
        wait.until(EC.url_contains("/my-account"))

        # Confirm successful login by verifying the URL
        if "/my-account" not in driver.current_url:
            self.fail("Login failed. URL does not contain '/my-account'. Current URL: {}".format(driver.current_url))

if __name__ == "__main__":
    unittest.main()