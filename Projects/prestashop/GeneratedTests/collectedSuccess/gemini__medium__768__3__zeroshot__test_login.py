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
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        email = "test@user.com"
        password = "test@user1"

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the login link in the top menu.
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the sign-in link: {e}")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "login-form"))
            )
        except Exception as e:
            self.fail(f"Login form did not load: {e}")

        # 4. Fill in the email and password fields.
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )

            email_field.send_keys(email)
            password_field.send_keys(password)

        except Exception as e:
            self.fail(f"Could not find or fill email/password fields: {e}")

        # 5. Submit the login form.
        try:
            submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "submit-login"))
            )
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the submit button: {e}")

        # 6. Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
            )
            self.assertIn("Sign out", sign_out_link.text)

        except Exception as e:
            self.fail(f"Login failed. Could not find 'Sign out' link: {e}")

if __name__ == "__main__":
    unittest.main()