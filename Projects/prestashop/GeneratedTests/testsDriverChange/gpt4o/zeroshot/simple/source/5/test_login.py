import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on 'Sign in' link
        try:
            sign_in_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Sign in link not found: {e}")

        # Fill in email
        try:
            email_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys("test@user.com")
        except Exception as e:
            self.fail(f"Email field not found: {e}")

        # Fill in password
        try:
            password_field = driver.find_element(By.ID, "field-password")
            password_field.send_keys("test@user1")
        except Exception as e:
            self.fail(f"Password field not found: {e}")

        # Click on 'Sign in' button
        try:
            sign_in_button = driver.find_element(By.ID, "submit-login")
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Sign in button not found: {e}")

        # Confirm success by checking the presence of 'Sign out'
        try:
            sign_out_text = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_text.is_displayed())
        except Exception as e:
            self.fail(f"Sign out text not found or login failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()