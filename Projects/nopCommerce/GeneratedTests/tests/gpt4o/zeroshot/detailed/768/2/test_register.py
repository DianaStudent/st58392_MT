import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        
        # Click the "Register" link in the top navigation
        register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        if not register_link:
            self.fail("Register link not found")
        register_link.click()
        
        # Wait for the registration form to load
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-page")))

        # Select "Female" gender
        gender_female_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        if not gender_female_radio:
            self.fail("Gender female radio button not found")
        gender_female_radio.click()

        # Fill in the required fields
        first_name = driver.find_element(By.ID, "FirstName")
        if not first_name:
            self.fail("First name input not found")
        first_name.send_keys("Test")

        last_name = driver.find_element(By.ID, "LastName")
        if not last_name:
            self.fail("Last name input not found")
        last_name.send_keys("User")

        email = driver.find_element(By.ID, "Email")
        if not email:
            self.fail("Email input not found")
        email.send_keys(f"testuser_{int(time.time())}@example.com")

        company = driver.find_element(By.ID, "Company")
        if not company:
            self.fail("Company input not found")
        company.send_keys("TestCorp")

        password = driver.find_element(By.ID, "Password")
        if not password:
            self.fail("Password input not found")
        password.send_keys("test11")

        confirm_password = driver.find_element(By.ID, "ConfirmPassword")
        if not confirm_password:
            self.fail("Confirm password input not found")
        confirm_password.send_keys("test11")

        # Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        if not register_button:
            self.fail("Register button not found")
        register_button.click()

        # Wait for the response page or confirmation message to load
        registration_result = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page")))

        # Verify that registration succeeded
        success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        if not success_message or "Your registration completed" not in success_message.text:
            self.fail("Registration success message not found or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()