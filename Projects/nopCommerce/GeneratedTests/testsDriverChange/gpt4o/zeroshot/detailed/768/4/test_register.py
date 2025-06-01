import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Step 1: Open the homepage (Handled in setUp)
        
        # Step 2: Click the "Register" link in the top navigation.
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Register'))
        )
        register_link.click()

        # Step 3: Wait for the registration form to load.
        register_form = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'gender-female'))
        )

        # Step 4: Select the gender.
        gender_female = driver.find_element(By.ID, 'gender-female')
        gender_female.click()

        # Step 5: Fill in the registration fields.
        first_name = driver.find_element(By.ID, 'FirstName')
        last_name = driver.find_element(By.ID, 'LastName')

        # Generate a dynamic email
        email = driver.find_element(By.ID, 'Email')
        dynamic_email = f"testuser_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@example.com"

        company = driver.find_element(By.ID, 'Company')
        password = driver.find_element(By.ID, 'Password')
        confirm_password = driver.find_element(By.ID, 'ConfirmPassword')

        first_name.send_keys('Test')
        last_name.send_keys('User')
        email.send_keys(dynamic_email)
        company.send_keys('TestCorp')
        password.send_keys('test11')
        confirm_password.send_keys('test11')

        # Step 6: Submit the registration form.
        register_button = driver.find_element(By.ID, 'register-button')
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load.
        registration_success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'result'))
        )

        # Step 8: Verify registration success.
        self.assertIsNotNone(registration_success_message)
        self.assertIn("Your registration completed", registration_success_message.text)

if __name__ == "__main__":
    unittest.main()