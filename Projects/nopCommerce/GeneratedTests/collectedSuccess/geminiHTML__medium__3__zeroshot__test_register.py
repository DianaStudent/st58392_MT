import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the "Register" link.
        try:
            register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except NoSuchElementException:
            self.fail("Register link not found.")

        # 3. Wait for the registration page to load.
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-page")))
        except NoSuchElementException:
            self.fail("Registration page not loaded.")

        # 4. Fill all the fields.
        try:
            # Gender: Female
            female_radio = self.wait.until(EC.element_to_be_clickable((By.ID, "gender-female")))
            female_radio.click()

            # First name: Test
            first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
            first_name_input.send_keys("Test")

            # Last name: User
            last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "LastName")))
            last_name_input.send_keys("User")

            # Email: dynamically generated
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
            email = "testuser" + str(int(time.time())) + "@example.com"
            email_input.send_keys(email)

            # Company: TestCorp
            company_input = self.wait.until(EC.presence_of_element_located((By.ID, "Company")))
            company_input.send_keys("TestCorp")

            # Password: test11
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "Password")))
            password_input.send_keys("test11")

            # Confirm Password: test11
            confirm_password_input = self.wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
            confirm_password_input.send_keys("test11")

        except NoSuchElementException:
            self.fail("One or more input fields not found.")

        # 5. Submit the registration form.
        try:
            register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            register_button.click()
        except NoSuchElementException:
            self.fail("Register button not found.")

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        try:
            result_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            result_text = result_element.text
            self.assertIn("Your registration completed", result_text)
        except NoSuchElementException:
            self.fail("Registration result message not found.")

if __name__ == "__main__":
    unittest.main()