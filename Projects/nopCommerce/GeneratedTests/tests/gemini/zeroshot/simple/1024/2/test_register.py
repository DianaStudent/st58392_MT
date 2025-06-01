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
        # Find and click the 'Register' link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Register' link: {e}")

        # Generate a unique email address
        email = f"test_{uuid.uuid4()}@example.com"
        password = "test11"

        # Locate and fill in the registration form fields
        try:
            gender_male = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            )
            gender_male.click()

            first_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name.send_keys("John")

            last_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name.send_keys("Doe")

            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_field.send_keys(email)

            company_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_name.send_keys("Test Company")

            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Newsletter"))
            )
            # Checkbox is checked by default, no need to click

            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_field.send_keys(password)

            confirm_password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_field.send_keys(password)

            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
            register_button.click()

        except Exception as e:
            self.fail(f"Could not find or interact with registration form elements: {e}")

        # Verify successful registration
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
            self.assertTrue(success_message.is_displayed(), "Success message is not displayed.")
        except Exception as e:
            self.fail(f"Registration was not successful or success message not found: {e}")

if __name__ == "__main__":
    unittest.main()