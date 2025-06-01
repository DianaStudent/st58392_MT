import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Navigate to the login page
        try:
            sign_in_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'Sign in': {e}")

        # Enter email
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys("test@user.com")
        except Exception as e:
            self.fail(f"Failed to find or interact with email input: {e}")

        # Enter password
        try:
            password_input = driver.find_element(By.ID, "field-password")
            password_input.send_keys("test@user1")
        except Exception as e:
            self.fail(f"Failed to find or interact with password input: {e}")

        # Submit the form
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except Exception as e:
            self.fail(f"Failed to click 'Sign in' button: {e}")

        # Check for "Sign out" link
        try:
            sign_out_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link not found; login may have failed.")
        except Exception as e:
            self.fail(f"Failed to find 'Sign out' link: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()