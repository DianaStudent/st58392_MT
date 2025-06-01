import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


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
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Register' link: {e}")

        # Generate a unique email address
        email = f"test_{uuid.uuid4()}@example.com"

        # Fill in the registration form
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            ).click()
        except Exception as e:
            self.fail(f"Could not find or click the 'gender-male' radio button: {e}")

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")
        except Exception as e:
            self.fail(f"Could not find or enter text into the 'FirstName' field: {e}")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")
        except Exception as e:
            self.fail(f"Could not find or enter text into the 'LastName' field: {e}")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)
        except Exception as e:
            self.fail(f"Could not find or enter text into the 'Email' field: {e}")

        try:
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("Acme Corp")
        except Exception as e:
            self.fail(f"Could not find or enter text into the 'Company' field: {e}")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")
        except Exception as e:
            self.fail(f"Could not find or enter text into the 'Password' field: {e}")

        try:
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")
        except Exception as e:
            self.fail(f"Could not find or enter text into the 'ConfirmPassword' field: {e}")

        # Click the 'Register' button
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Register' button: {e}")

        # Verify successful registration
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
        except Exception as e:
            self.fail(f"Registration was not successful. Could not find success message: {e}")