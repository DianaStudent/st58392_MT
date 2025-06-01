import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
        except NoSuchElementException:
            self.fail("Register link not found on the homepage.")

        # 3. Wait for the registration page to load.
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-page")))

        # 4. Fill all the fields.
        try:
            # Gender: Female
            female_radio = wait.until(EC.element_to_be_clickable((By.ID, "gender-female")))
            female_radio.click()

            # First name: Test
            first_name_input = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
            first_name_input.send_keys("Test")

            # Last name: User
            last_name_input = wait.until(EC.presence_of_element_located((By.ID, "LastName")))
            last_name_input.send_keys("User")

            # Email: dynamically generated
            email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            email = "testuser" + str(time.time()) + "@example.com"
            email_input.send_keys(email)

            # Company: TestCorp
            company_input = wait.until(EC.presence_of_element_located((By.ID, "Company")))
            company_input.send_keys("TestCorp")

            # Password: test11
            password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
            password_input.send_keys("test11")

            # Confirm password: test11
            confirm_password_input = wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
            confirm_password_input.send_keys("test11")

        except NoSuchElementException as e:
            self.fail(f"Could not find element: {e}")

        # 5. Submit the registration form.
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            register_button.click()
        except NoSuchElementException:
            self.fail("Register button not found.")

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        try:
            result_message_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            result_message_text = result_message_element.text
            self.assertIn("Your registration completed", result_message_text)
        except NoSuchElementException:
            self.fail("Registration result message not found.")
        except AssertionError:
            self.fail(f"Expected 'Your registration completed' in '{result_message_text}' but it was not found.")


if __name__ == "__main__":
    unittest.main()