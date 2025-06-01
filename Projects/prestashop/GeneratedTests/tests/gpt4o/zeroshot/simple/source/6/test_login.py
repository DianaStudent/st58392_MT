import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver

        # Click on Sign in link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Sign in link not found: {str(e)}")

        # Fill in email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys("test@user.com")
        except Exception as e:
            self.fail(f"Email input not found: {str(e)}")

        # Fill in password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys("test@user1")
        except Exception as e:
            self.fail(f"Password input not found: {str(e)}")

        # Click on Sign in button
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "submit-login"))
            )
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Sign in button not found: {str(e)}")

        # Check for 'Sign out' text to confirm successful login
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except Exception as e:
            self.fail(f"Sign out link not found, login may have failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()