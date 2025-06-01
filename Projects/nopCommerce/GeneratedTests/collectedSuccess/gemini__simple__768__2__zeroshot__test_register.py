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
            self.fail(f"Failed to find or click 'My account' link: {e}")

        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Register' link: {e}")
        
        # Generate unique email
        email = str(uuid.uuid4()) + "@example.com"

        # Fill registration form
        try:
            male_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            male_radio.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Male' radio button: {e}")

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'First Name' input: {e}")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Last Name' input: {e}")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Email' input: {e}")

        try:
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("Acme Corp")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Company' input: {e}")

        try:
            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Newsletter"))
            )
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Newsletter' checkbox: {e}")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Password' input: {e}")

        try:
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Confirm Password' input: {e}")

        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Register' button: {e}")

        # Verify registration success
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
        except Exception as e:
            self.fail(f"Registration failed or success message not found: {e}")

if __name__ == "__main__":
    unittest.main()