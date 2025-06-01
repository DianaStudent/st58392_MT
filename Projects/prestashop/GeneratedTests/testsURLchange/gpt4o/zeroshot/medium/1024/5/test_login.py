import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver

        # Click on the "Sign in" link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except Exception:
            self.fail("Could not find 'Sign in' link or click failed.")

        # Wait for the login form to appear
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
        except Exception:
            self.fail("Login form did not load.")

        # Fill in the email and password fields
        email_field.send_keys("test@user.com")

        try:
            password_field = driver.find_element(By.ID, "field-password")
            password_field.send_keys("test@user1")
        except Exception:
            self.fail("Could not find or fill in the password field.")

        # Submit the login form
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except Exception:
            self.fail("Could not find or click the submit button.")

        # Check for "Sign out" to verify successful login
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertIsNotNone(sign_out_link, "Login was unsuccessful. 'Sign out' not found.")
        except Exception:
            self.fail("Login failed, 'Sign out' not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()