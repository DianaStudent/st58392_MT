from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You may need to specify the path to chromedriver
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        
        # Find and click on the 'Sign in' link
        try:
            sign_in_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Sign in']]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find 'Sign in' link: {e}")

        # Wait for login form to be visible
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.ID, "login-form"))
            )
        except Exception as e:
            self.fail(f"Login form did not appear: {e}")

        # Fill email and password
        try:
            email_input = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']"))
            )
            password_input = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
            )
            email_input.send_keys("test@user.com")
            password_input.send_keys("test@user1")
        except Exception as e:
            self.fail(f"Error interacting with the login form: {e}")

        # Submit the login form
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, "button#submit-login")
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not click login button: {e}")

        # Confirm success by checking the presence of "Sign out"
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[span[text()='Sign out']]"))
            )
        except Exception as e:
            self.fail(f"Login was not successful, 'Sign out' link not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()