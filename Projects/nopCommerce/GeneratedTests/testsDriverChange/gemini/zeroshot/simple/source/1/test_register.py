import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import uuid

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        try:
            # Navigate to registration page
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            # Generate a unique email
            unique_id = str(uuid.uuid4())
            email = f"test_{unique_id}@example.com"

            # Fill in registration form
            male_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            male_radio.click()

            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)

            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("Test Company")

            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Newsletter"))
            )
            # Checkbox is checked by default, no need to click

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")

            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")

            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()

            # Verify registration success
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
            self.assertTrue("Your registration completed" in success_message.text)

        except TimeoutException:
            self.fail("Timeout occurred while waiting for an element.")
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()