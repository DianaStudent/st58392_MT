import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def generate_email(self):
        # Generate a random email
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            gender_male_radio = wait.until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            )
            gender_male_radio.click()

            first_name_input = driver.find_element(By.ID, "FirstName")
            last_name_input = driver.find_element(By.ID, "LastName")
            email_input = driver.find_element(By.ID, "Email")
            password_input = driver.find_element(By.ID, "Password")
            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")

            if not all([first_name_input, last_name_input, email_input, password_input, confirm_password_input]):
                self.fail("One or more required input fields are missing.")

            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            email_input.send_keys(self.generate_email())
            password_input.send_keys("test11")
            confirm_password_input.send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")

            if not register_button:
                self.fail("Register button is missing.")

            register_button.click()

            registration_success_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )

            self.assertEqual(registration_success_message.text, "Your registration completed")

        except TimeoutException:
            self.fail("Element could not be located or action could not be completed within the time frame.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()