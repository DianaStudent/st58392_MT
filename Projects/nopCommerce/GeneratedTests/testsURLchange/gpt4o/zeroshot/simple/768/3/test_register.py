import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver

        # Navigate to registration page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail("Failed to find 'My account' link: " + str(e))

        # Fill out registration form
        try:
            gender_male_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            )
            gender_male_radio.click()

            first_name_field = driver.find_element(By.ID, "FirstName")
            first_name_field.send_keys("TestFirstName")

            last_name_field = driver.find_element(By.ID, "LastName")
            last_name_field.send_keys("TestLastName")

            email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"
            email_field = driver.find_element(By.ID, "Email")
            email_field.send_keys(email)

            password_field = driver.find_element(By.ID, "Password")
            password_field.send_keys("test11")

            confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_field.send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

        except Exception as e:
            self.fail("Failed during registration process: " + str(e))

        # Confirm registration success
        try:
            registration_success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.result"))
            )
            self.assertEqual(registration_success_message.text, "Your registration completed")
        except Exception as e:
            self.fail("Registration success message not found or incorrect: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()