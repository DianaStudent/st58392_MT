from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Step 1: Click the "Register" link in the top navigation
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
        register_link.click()

        # Step 2-4: Wait for the registration form to load and fill in all required fields
        self.fill_registration_form(
            first_name="Test",
            last_name="User",
            email=self.generate_email(),
            company="TestCorp",
            password="test11",
            confirm_password="test11"
        )

        # Step 5: Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Step 6-7: Wait for the response page or confirmation message to load and verify that registration succeeded
        self.verify_registration_succeeded()

    def generate_email(self):
        import uuid
        return f"test{uuid.uuid4().int}{uuid.uuid4().int}@example.com"

    def fill_registration_form(self, first_name, last_name, email, company, password, confirm_password):
        # Select the appropriate gender radio input based on the provided data (assuming "Female")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='gender' and @value='female']"))).click()

        # Fill in all required fields
        self.fill_input_field(first_name, "first_name", "//input[@id='first_name']")
        self.fill_input_field(last_name, "last_name", "//input[@id='last_name']")
        self.fill_input_field(email, "email", "//input[@id='email']")
        self.fill_input_field(company, "company", "//input[@id='company']")
        self.fill_password_fields(password, confirm_password)

    def fill_input_field(self, value, field_name, locator):
        input_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator)))
        if not input_field.is_enabled():
            self.fail(f"{field_name} is not enabled")
        input_field.send_keys(value)

    def fill_password_fields(self, password, confirm_password):
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        confirm_password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='confirm_password']")))
        if not password_input.is_enabled() or not confirm_password_input.is_enabled():
            self.fail("Password fields are not enabled")
        password_input.send_keys(password)
        confirm_password_input.send_keys(confirm_password)

    def verify_registration_succeeded(self):
        # Wait for the response page or confirmation message to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))

        # Check if a confirmation text element is present with content including "Your registration completed"
        result_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        if not result_element.is_displayed() or not result_element.text:
            self.fail("Registration failed")
        if not ("Your registration completed" in result_element.text):
            self.fail("Confirmation text does not match expected content")

if __name__ == "__main__":
    unittest.main()