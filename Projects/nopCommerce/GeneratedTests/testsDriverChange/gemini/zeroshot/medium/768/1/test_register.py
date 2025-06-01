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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the "Register" link.
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # 3. Wait for the registration page to load.
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-page")))

        # 4. Fill all the fields.
        # Gender
        female_radio = self.wait.until(EC.element_to_be_clickable((By.ID, "gender-female")))
        female_radio.click()

        # First name
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        first_name_input.send_keys("Test")

        # Last name
        last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "LastName")))
        last_name_input.send_keys("User")

        # Email
        email = "test_user_" + str(uuid.uuid4()) + "@example.com"
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_input.send_keys(email)

        # Company
        company_input = self.wait.until(EC.presence_of_element_located((By.ID, "Company")))
        company_input.send_keys("TestCorp")

        # Password
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_input.send_keys("test11")

        # Confirm password
        confirm_password_input = self.wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
        confirm_password_input.send_keys("test11")

        # 5. Submit the registration form.
        register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
        register_button.click()

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        registration_result_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page")))
        if registration_result_element:
            result_message_element = self.driver.find_element(By.CLASS_NAME, "result")
            if result_message_element:
                result_message_text = result_message_element.text
                if result_message_text:
                    self.assertIn("Your registration completed", result_message_text)
                else:
                    self.fail("Result message text is empty.")
            else:
                self.fail("Result message element not found.")
        else:
            self.fail("Registration result page element not found.")

if __name__ == "__main__":
    unittest.main()