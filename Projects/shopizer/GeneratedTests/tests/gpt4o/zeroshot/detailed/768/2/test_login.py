import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies if the button exists
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if cookie_button and cookie_button.is_displayed():
                cookie_button.click()
        except:
            pass  # Ignore if it doesn't exist

        # Click on the account icon/button
        account_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.account-setting-active")))
        if not account_button:
            self.fail("Account button not found")
        account_button.click()

        # Click "Login" in the dropdown
        login_link = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Login")))
        if not login_link:
            self.fail("Login link not found in dropdown")
        login_link.click()

        # Wait for the login form to appear
        username_field = wait.until(EC.presence_of_element_located(
            (By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located(
            (By.NAME, "loginPassword")))

        if not username_field or not password_field:
            self.fail("Login form fields are missing")

        # Fill in login credentials
        username_field.send_keys("test2@user.com")
        password_field.send_keys("test**11")

        # Submit the form
        login_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")))
        if not login_button:
            self.fail("Login button not found")
        login_button.click()

        # Verify redirection to /my-account
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()