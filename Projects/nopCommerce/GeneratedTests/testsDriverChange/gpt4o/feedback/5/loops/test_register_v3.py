from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import uuid
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Use ChromeDriverManager to manage the ChromeDriver automatically
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver

        # Step 2: Click the "Register" link
        register_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        if register_link is None or not register_link.is_displayed():
            self.fail("Register link not found or not displayed")
        register_link.click()

        # Step 3: Wait for the registration form to load
        registration_form = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.page.registration-page"))
        )
        if registration_form is None or not registration_form.is_displayed():
            self.fail("Registration form did not load")

        # Step 4: Select gender
        gender_female = driver.find_element(By.ID, "gender-female")
        if gender_female is None or not gender_female.is_displayed():
            self.fail("Gender female radio button not found or not displayed")
        gender_female.click()

        # Step 5: Fill in all required fields
        first_name_field = driver.find_element(By.ID, "FirstName")
        if first_name_field is None or not first_name_field.is_displayed():
            self.fail("First name field not found or not displayed")
        first_name_field.send_keys("Test")

        last_name_field = driver.find_element(By.ID, "LastName")
        if last_name_field is None or not last_name_field.is_displayed():
            self.fail("Last name field not found or not displayed")
        last_name_field.send_keys("User")

        # Generating a unique email
        email = f"test+{uuid.uuid4()}@example.com"
        email_field = driver.find_element(By.ID, "Email")
        if email_field is None or not email_field.is_displayed():
            self.fail("Email field not found or not displayed")
        email_field.send_keys(email)

        company_field = driver.find_element(By.ID, "Company")
        if company_field is None or not company_field.is_displayed():
            self.fail("Company field not found or not displayed")
        company_field.send_keys("TestCorp")

        password_field = driver.find_element(By.ID, "Password")
        if password_field is None or not password_field.is_displayed():
            self.fail("Password field not found or not displayed")
        password_field.send_keys("test11")

        confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
        if confirm_password_field is None or not confirm_password_field.is_displayed():
            self.fail("Confirm password field not found or not displayed")
        confirm_password_field.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        if register_button is None or not register_button.is_displayed():
            self.fail("Register button not found or not displayed")
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        result_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.result"))
        )
        if result_message is None or not result_message.is_displayed():
            self.fail("Registration result message not found or not displayed")

        # Step 8: Verify that registration was successful
        self.assertIn("Your registration completed", result_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()