from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Step 1: Open the homepage is already done in setUp.

        # Step 2: Click the login link from the top navigation.
        login_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info a"))
        )
        login_link.click()

        # Step 3: Wait for the login page to load.
        self.wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields.
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")

        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Step 5: Click the submit button.
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login.
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-info")))

        # Step 7: Confirm that login was successful.
        try:
            sign_out_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout"))
            )
            account_name = driver.find_element(By.CSS_SELECTOR, "a.account span.hidden-sm-down")
            self.assertIn("Sign out", sign_out_button.text)
            self.assertIn("test user", account_name.text)
        except Exception as e:
            self.fail(f"Login failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()