from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import uuid
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver

        # Click the "Register" link
        register_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        if register_link is None or not register_link.is_displayed():
            self.fail("Register link not found or not displayed")
        register_link.click()

        # Wait for the registration form to load
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.page.registration-page"))
        )

        # Select gender
        gender_female = self.wait.until(
            EC.presence_of_element_located((By.ID, "gender-female"))
        )
        if gender_female is None or not gender_female.is_displayed():
            self.fail("Gender female radio button not found or not displayed")
        gender_female.click()

        # Fill in all required fields
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "FirstName"))
        )
        if first_name_field is None or not first_name_field.is_displayed():
            self.fail("First name field not found or not displayed")
        first_name_field.send_keys("Test")

        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "LastName"))
        )
        if last_name_field is None or not last_name_field.is_displayed():
            self.fail("Last name field not found or not displayed")
        last_name_field.send_keys("User")

        # Generate unique email
        email = f"test+{uuid.uuid4()}@example.com"
        email_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        if email_field is None or not email_field.is_displayed():
            self.fail("Email field not found or not displayed")
        email_field.send_keys(email)

        company_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "Company"))
        )
        if company_field is None or not company_field.is_displayed():
            self.fail("Company field not found or not displayed")
        company_field.send_keys("TestCorp")

        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "Password"))
        )
        if password_field is None or not password_field.is_displayed():
            self.fail("Password field not found or not displayed")
        password_field.send_keys("test11")

        confirm_password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "ConfirmPassword"))
        )
        if confirm_password_field is None or not confirm_password_field.is_displayed():
            self.fail("Confirm password field not found or not displayed")
        confirm_password_field.send_keys("test11")

        # Submit the registration form
        register_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "register-button"))
        )
        if register_button is None or not register_button.is_displayed():
            self.fail("Register button not found or not displayed")
        register_button.click()

        # Verify registration success
        result_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.result"))
        )
        if result_message is None or not result_message.is_displayed():
            self.fail("Registration result message not found or not displayed")
        self.assertIn("Your registration completed", result_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()