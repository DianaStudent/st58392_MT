import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual URL

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the registration page
        my_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        my_account_link.click()

        # Generate a random email
        random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

        # Interact with the registration form
        try:
            gender_male_radio = wait.until(EC.presence_of_element_located((By.ID, "gender-male")))
            gender_male_radio.click()

            first_name_field = driver.find_element(By.ID, "FirstName")
            first_name_field.send_keys("Test")

            last_name_field = driver.find_element(By.ID, "LastName")
            last_name_field.send_keys("User")

            email_field = driver.find_element(By.ID, "Email")
            email_field.send_keys(random_email)

            company_field = driver.find_element(By.ID, "Company")
            company_field.send_keys("Test Company")

            newsletter_checkbox = driver.find_element(By.ID, "Newsletter")
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()

            password_field = driver.find_element(By.ID, "Password")
            password_field.send_keys("test11")

            confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_field.send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Confirm success message
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertIn("Your registration completed", success_message.text)

        except Exception as e:
            self.fail(f"Test failed due to missing element or unexpected error: {str(e)}")

if __name__ == "__main__":
    unittest.main()