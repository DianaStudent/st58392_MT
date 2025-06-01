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
        # Navigate to registration page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Register' link: {e}")

        # Generate a unique email address
        unique_id = str(uuid.uuid4())
        email = f"test_{unique_id}@example.com"

        # Fill in registration form
        try:
            male_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            male_radio.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Male' radio button: {e}")

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")
        except Exception as e:
            self.fail(f"Could not find or enter text into 'FirstName' input: {e}")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")
        except Exception as e:
            self.fail(f"Could not find or enter text into 'LastName' input: {e}")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)
        except Exception as e:
            self.fail(f"Could not find or enter text into 'Email' input: {e}")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")
        except Exception as e:
            self.fail(f"Could not find or enter text into 'Password' input: {e}")

        try:
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")
        except Exception as e:
            self.fail(f"Could not find or enter text into 'ConfirmPassword' input: {e}")

        # Submit the form
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Register' button: {e}")

        # Verify registration success
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
            self.assertTrue(success_message.is_displayed(), "Registration success message is not displayed.")
        except Exception as e:
            self.fail(f"Registration failed or success message not found: {e}")

if __name__ == "__main__":
    unittest.main()