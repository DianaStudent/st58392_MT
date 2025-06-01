import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_user_registration(self):
        driver = self.driver

        # Navigate to 'Register' page
        my_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()

        # Fill in registration form
        try:
            first_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            last_name = driver.find_element(By.ID, "LastName")
            email = driver.find_element(By.ID, "Email")
            password = driver.find_element(By.ID, "Password")
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")

            # Generate a random email
            generated_email = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@example.com"

            # Fill in the fields
            first_name.send_keys("TestFirstName")
            last_name.send_keys("TestLastName")
            email.send_keys(generated_email)
            password.send_keys("test11")
            confirm_password.send_keys("test11")

            # Submit the form
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Verify registration success
            registration_result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            self.assertIn("Your registration completed", registration_result.text)
        
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()