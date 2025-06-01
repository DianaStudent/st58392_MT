import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the "Register" link.
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'Register' link: {e}")

        # 3. Wait for the registration page to load.
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-page")))
        except Exception as e:
            self.fail(f"Registration page did not load: {e}")

        # 4. Fill all the fields.
        try:
            female_radio = wait.until(EC.element_to_be_clickable((By.ID, "gender-female")))
            female_radio.click()

            first_name_input = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
            first_name_input.send_keys("Test")

            last_name_input = wait.until(EC.presence_of_element_located((By.ID, "LastName")))
            last_name_input.send_keys("User")

            email = f"test.user{uuid.uuid4()}@example.com"
            email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            email_input.send_keys(email)

            company_input = wait.until(EC.presence_of_element_located((By.ID, "Company")))
            company_input.send_keys("TestCorp")

            password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
            password_input.send_keys("test11")

            confirm_password_input = wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
            confirm_password_input.send_keys("test11")

        except Exception as e:
            self.fail(f"Failed to fill registration form: {e}")

        # 5. Submit the registration form.
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to submit registration form: {e}")

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        try:
            result_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page")))
            if result_element:
                result_text_element = driver.find_element(By.CLASS_NAME, "result")
                if result_text_element:
                    result_text = result_text_element.text
                    self.assertIn("Your registration completed", result_text)
                else:
                    self.fail("Result text element not found.")
            else:
                self.fail("Registration result page not found.")
        except Exception as e:
            self.fail(f"Registration completion message not found: {e}")

if __name__ == "__main__":
    unittest.main()