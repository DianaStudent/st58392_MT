import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")  # Replace with the actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_process(self):
        driver = self.driver

        # Step 1: Open the homepage (already done in setUp)

        # Step 2: Click the "Register" link in the top navigation
        register_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[@href='/customer/info']")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")
        register_link.click()

        # Step 3: Wait for the registration form to load
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page registration-page']")))

        # Step 4: Select the appropriate gender radio input
        gender_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        self.assertTrue(gender_radio.is_displayed(), "Gender radio input is not visible")
        gender_radio.click()

        # Create a dynamic email
        dynamic_email = f"testuser_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"

        # Step 5: Fill in all required fields
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        self.assertTrue(first_name_input.is_displayed(), "First name input is not visible")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, "LastName")
        self.assertTrue(last_name_input.is_displayed(), "Last name input is not visible")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, "Email")
        self.assertTrue(email_input.is_displayed(), "Email input is not visible")
        email_input.send_keys(dynamic_email)

        company_input = driver.find_element(By.ID, "Company")
        self.assertTrue(company_input.is_displayed(), "Company input is not visible")
        company_input.send_keys("TestCorp")

        password_input = driver.find_element(By.ID, "Password")
        self.assertTrue(password_input.is_displayed(), "Password input is not visible")
        password_input.send_keys("test11")

        confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
        self.assertTrue(confirm_password_input.is_displayed(), "Confirm password input is not visible")
        confirm_password_input.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        confirmation_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        self.assertTrue(confirmation_message.is_displayed(), "Confirmation message is not visible")

        # Step 8: Verify that registration succeeded
        self.assertIn("Your registration completed", confirmation_message.text, "Registration did not succeed")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()