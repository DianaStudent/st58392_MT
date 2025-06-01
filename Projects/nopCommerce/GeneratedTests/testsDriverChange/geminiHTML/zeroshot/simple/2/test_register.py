import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Navigate to registration page. Assuming "My account" link leads to login/register
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link: {e}")

        # Assuming there's a registration link on the login page, but no HTML for it was provided.
        # So, I'll navigate directly to /register. This might need adjustment based on actual UI.
        driver.get("http://max/register")

        # Verify that the register page is loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
            )
        except Exception as e:
            self.fail(f"Registration page did not load correctly: {e}")

        # Generate a random email
        email = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@example.com"

        # Fill in the registration form
        try:
            # Gender
            male_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            male_radio.click()

            # First name
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")

            # Last name
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")

            # Email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)

            # Company (optional)
            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("Example Company")

            # Newsletter (already checked, no action needed)

            # Password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")

            # Confirm password
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")

            # Register button
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()

        except Exception as e:
            self.fail(f"Failed to fill and submit the registration form: {e}")

        # Verify successful registration
        try:
            result_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
            self.assertTrue("Your registration completed" in result_element.text)

        except Exception as e:
            self.fail(f"Registration failed or success message not found: {e}")

if __name__ == "__main__":
    unittest.main()