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

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage.
        driver.get("http://max/")

        # 2. Click the "Register".
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        if not register_link.is_displayed():
            self.fail("Register link is not displayed.")
        
        register_link.click()

        # 3. Wait for the registration page to load.
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page.registration-page")))

        # 4. Fill all the fields.
        # Generate a dynamic email
        dynamic_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@test.com"
        
        # Select Female gender
        gender_female = driver.find_element(By.ID, "gender-female")
        if not gender_female.is_displayed():
            self.fail("Gender female radio button is not displayed.")
        gender_female.click()

        # Enter First name
        first_name = driver.find_element(By.ID, "FirstName")
        if not first_name.is_displayed():
            self.fail("First name field is not displayed.")
        first_name.send_keys("Test")

        # Enter Last name
        last_name = driver.find_element(By.ID, "LastName")
        if not last_name.is_displayed():
            self.fail("Last name field is not displayed.")
        last_name.send_keys("User")

        # Enter Email
        email = driver.find_element(By.ID, "Email")
        if not email.is_displayed():
            self.fail("Email field is not displayed.")
        email.send_keys(dynamic_email)

        # Enter Company
        company = driver.find_element(By.ID, "Company")
        if not company.is_displayed():
            self.fail("Company field is not displayed.")
        company.send_keys("TestCorp")

        # Enter Password
        password = driver.find_element(By.ID, "Password")
        if not password.is_displayed():
            self.fail("Password field is not displayed.")
        password.send_keys("test11")

        # Confirm Password
        confirm_password = driver.find_element(By.ID, "ConfirmPassword")
        if not confirm_password.is_displayed():
            self.fail("Confirm password field is not displayed.")
        confirm_password.send_keys("test11")

        # 5. Submit the registration form.
        register_button = driver.find_element(By.ID, "register-button")
        if not register_button.is_displayed():
            self.fail("Register button is not displayed.")
        register_button.click()

        # 6. Verify that a message like "Your registration completed" is shown after successful registration.
        registration_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
        registration_text = registration_result.text
        if not registration_text:
            self.fail("Registration result text is empty.")
        
        self.assertIn("Your registration completed", registration_text, "Registration success message not found.")

if __name__ == "__main__":
    unittest.main()