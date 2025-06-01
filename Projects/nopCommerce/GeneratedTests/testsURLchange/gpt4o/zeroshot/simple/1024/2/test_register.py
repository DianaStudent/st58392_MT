import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestUserRegistration(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@example.com"
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the registration page
        try:
            my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
            my_account_link.click()
        except:
            self.fail("Failed to find 'My account' link")

        try:
            register_form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        except:
            self.fail("Failed to locate the registration form")

        # Fill in the registration form
        try:
            gender_male = driver.find_element(By.ID, "gender-male")
            gender_male.click()

            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("John")

            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("Doe")

            email = driver.find_element(By.ID, "Email")
            email.send_keys(self.generate_random_email())

            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")

            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Failed to fill out the registration form")

        # Verify registration success
        try:
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertIn("Your registration completed", success_message.text)
        except:
            self.fail("Registration success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()