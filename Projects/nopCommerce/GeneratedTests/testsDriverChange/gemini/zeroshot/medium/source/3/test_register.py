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
        register_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        if register_link:
            register_link.click()
        else:
            self.fail("Register link not found on the homepage.")

        # 3. Wait for the registration page to load.
        wait.until(EC.title_contains("Register"))

        # 4. Fill all the fields.
        # Gender: Female
        female_gender_radio = wait.until(
            EC.presence_of_element_located((By.ID, "gender-female"))
        )
        if female_gender_radio:
            female_gender_radio.click()
        else:
            self.fail("Female gender radio button not found.")

        # First name: Test
        first_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "FirstName"))
        )
        if first_name_input:
            first_name_input.send_keys("Test")
        else:
            self.fail("First name input field not found.")

        # Last name: User
        last_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "LastName"))
        )
        if last_name_input:
            last_name_input.send_keys("User")
        else:
            self.fail("Last name input field not found.")

        # Email: dynamically generated
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        if email_input:
            email = f"testuser_{uuid.uuid4()}@example.com"
            email_input.send_keys(email)
        else:
            self.fail("Email input field not found.")

        # Company: TestCorp
        company_input = wait.until(
            EC.presence_of_element_located((By.ID, "Company"))
        )
        if company_input:
            company_input.send_keys("TestCorp")
        else:
            self.fail("Company input field not found.")

        # Password: test11
        password_input = wait.until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        if password_input:
            password_input.send_keys("test11")
        else:
            self.fail("Password input field not found.")

        # Confirm password: test11
        confirm_password_input = wait.until(
            EC.presence_of_element_located((By.ID, "ConfirmPassword"))
        )
        if confirm_password_input:
            confirm_password_input.send_keys("test11")
        else:
            self.fail("Confirm password input field not found.")

        # 5. Submit the registration form.
        register_button = wait.until(
            EC.presence_of_element_located((By.ID, "register-button"))
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found.")

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        registration_result = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "result"))
        )
        if registration_result:
            result_text = registration_result.text
            self.assertIn("Your registration completed", result_text, "Registration not completed successfully.")
        else:
            self.fail("Registration result message not found.")


if __name__ == "__main__":
    unittest.main()