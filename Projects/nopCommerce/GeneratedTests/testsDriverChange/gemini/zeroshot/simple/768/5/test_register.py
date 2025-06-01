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

        # Fill registration form
        try:
            gender_male = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            gender_male.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'gender-male' radio button: {e}")

        try:
            first_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name.send_keys("Test")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'FirstName' field: {e}")

        try:
            last_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name.send_keys("User")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'LastName' field: {e}")

        email_address = str(uuid.uuid4()) + "@example.com"
        try:
            email = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email.send_keys(email_address)
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Email' field: {e}")

        try:
            company = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company.send_keys("TestCompany")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Company' field: {e}")

        try:
            newsletter = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Newsletter"))
            )
            if not newsletter.is_selected():
                newsletter.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Newsletter' checkbox: {e}")

        try:
            password = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password.send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'Password' field: {e}")

        try:
            confirm_password = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password.send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to find or enter text into 'ConfirmPassword' field: {e}")

        # Submit registration form
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'register-button': {e}")

        # Verify successful registration
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
        except Exception as e:
            self.fail(f"Registration failed: {e}")

if __name__ == "__main__":
    unittest.main()