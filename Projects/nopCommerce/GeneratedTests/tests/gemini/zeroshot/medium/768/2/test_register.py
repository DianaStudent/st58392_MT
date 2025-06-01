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
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # 3. Wait for the registration page to load.
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
        )

        # 4. Fill all the fields.
        # Gender: Female
        female_radio = wait.until(
            EC.element_to_be_clickable((By.ID, "gender-female"))
        )
        if female_radio:
            female_radio.click()
        else:
            self.fail("Female radio button not found.")

        # First name: Test
        first_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "FirstName"))
        )
        if first_name_input:
            first_name_input.send_keys("Test")
        else:
            self.fail("First name input not found.")

        # Last name: User
        last_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "LastName"))
        )
        if last_name_input:
            last_name_input.send_keys("User")
        else:
            self.fail("Last name input not found.")

        # Email: dynamically generated
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        email = f"testuser{uuid.uuid4()}@example.com"
        if email_input:
            email_input.send_keys(email)
        else:
            self.fail("Email input not found.")

        # Company: TestCorp
        company_input = wait.until(
            EC.presence_of_element_located((By.ID, "Company"))
        )
        if company_input:
            company_input.send_keys("TestCorp")
        else:
            self.fail("Company input not found.")

        # Password: test11
        password_input = wait.until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        if password_input:
            password_input.send_keys("test11")
        else:
            self.fail("Password input not found.")

        # Confirm Password: test11
        confirm_password_input = wait.until(
            EC.presence_of_element_located((By.ID, "ConfirmPassword"))
        )
        if confirm_password_input:
            confirm_password_input.send_keys("test11")
        else:
            self.fail("Confirm password input not found.")

        # 5. Submit the registration form.
        register_button = wait.until(
            EC.element_to_be_clickable((By.ID, "register-button"))
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found.")

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        result_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
        )

        if result_element:
            result_text_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            if result_text_element:
                result_text = result_text_element.text
                self.assertIn("Your registration completed", result_text)
            else:
                self.fail("Result text element not found.")
        else:
            self.fail("Registration result page not found.")


if __name__ == "__main__":
    unittest.main()