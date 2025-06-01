from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import uuid
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        
        # Step 2: Click the "Register" link
        register_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        self.assertIsNotNone(register_link)
        register_link.click()

        # Step 3: Wait for the registration form to load
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.page.registration-page"))
        )

        # Step 4: Select gender
        gender_female = driver.find_element(By.ID, "gender-female")
        self.assertIsNotNone(gender_female)
        gender_female.click()

        # Step 5: Fill in all required fields
        first_name_field = driver.find_element(By.ID, "FirstName")
        self.assertIsNotNone(first_name_field)
        first_name_field.send_keys("Test")

        last_name_field = driver.find_element(By.ID, "LastName")
        self.assertIsNotNone(last_name_field)
        last_name_field.send_keys("User")

        # Generating a unique email
        email = f"test+{uuid.uuid4()}@example.com"
        email_field = driver.find_element(By.ID, "Email")
        self.assertIsNotNone(email_field)
        email_field.send_keys(email)

        company_field = driver.find_element(By.ID, "Company")
        self.assertIsNotNone(company_field)
        company_field.send_keys("TestCorp")

        password_field = driver.find_element(By.ID, "Password")
        self.assertIsNotNone(password_field)
        password_field.send_keys("test11")

        confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
        self.assertIsNotNone(confirm_password_field)
        confirm_password_field.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        self.assertIsNotNone(register_button)
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        result_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.result"))
        )
        self.assertIsNotNone(result_message)

        # Step 8: Verify that registration was successful
        self.assertIn("Your registration completed", result_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()