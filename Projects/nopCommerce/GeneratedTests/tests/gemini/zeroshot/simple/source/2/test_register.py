import unittest
import time
import random
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
        try:
            # Find and click the 'Register' link
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            # Verify that we are on the registration page
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']"))
            )

            # Generate a random email
            email = f"test{random.randint(1000, 9999)}@example.com"

            # Fill in the registration form
            male_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
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
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")

            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")

            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
            register_button.click()

            # Verify successful registration
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result'][contains(text(), 'Your registration completed')]"))
            )
            self.assertIn("Your registration completed", success_message.text)

        except Exception as e:
            self.fail(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    unittest.main()