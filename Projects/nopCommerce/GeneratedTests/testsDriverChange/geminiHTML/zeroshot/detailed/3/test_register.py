import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # 1. Open the homepage.
        # 2. Click the "Register" link in the top navigation.
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except NoSuchElementException:
            self.fail("Register link not found.")

        # 3. Wait for the registration form to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
        except NoSuchElementException:
            self.fail("Registration form not loaded.")

        # 4. Select the appropriate gender radio input based on the provided data.
        try:
            female_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-female"))
            )
            female_radio.click()
        except NoSuchElementException:
            self.fail("Female radio button not found.")

        # 5. Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("Test")
        except NoSuchElementException:
            self.fail("First name input not found.")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("User")
        except NoSuchElementException:
            self.fail("Last name input not found.")

        email = "testuser" + str(int(time.time())) + "@example.com"
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)
        except NoSuchElementException:
            self.fail("Email input not found.")

        try:
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("TestCorp")
        except NoSuchElementException:
            self.fail("Company input not found.")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")
        except NoSuchElementException:
            self.fail("Password input not found.")

        try:
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")
        except NoSuchElementException:
            self.fail("Confirm password input not found.")

        # 6. Submit the registration form.
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
            register_button.click()
        except NoSuchElementException:
            self.fail("Register button not found.")

        # 7. Wait for the response page or confirmation message to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
            )
        except NoSuchElementException:
            self.fail("Registration result page not loaded.")

        # 8. Verify that registration succeeded by checking:
        #    - A confirmation text element is present - Its content includes "Your registration completed".
        try:
            result_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            result_text = result_element.text
            self.assertIn("Your registration completed", result_text)
        except NoSuchElementException:
            self.fail("Registration result message not found.")

if __name__ == "__main__":
    unittest.main()