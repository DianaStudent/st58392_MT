import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.set_window_size(1920, 1080)
    
    def get_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to registration page
            account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            account_link.click()

            # Fill in registration form
            first_name = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
            last_name = driver.find_element(By.ID, "LastName")
            email = driver.find_element(By.ID, "Email")
            password = driver.find_element(By.ID, "Password")
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")

            if not (first_name and last_name and email and password and confirm_password):
                self.fail("One or more form fields are missing")

            first_name.send_keys("TestFirstName")
            last_name.send_keys("TestLastName")
            email.send_keys(self.get_random_email())
            password.send_keys("test11")
            confirm_password.send_keys("test11")

            # Click register button
            register_button = driver.find_element(By.ID, "register-button")
            if not register_button:
                self.fail("Register button is missing")
                
            register_button.click()

            # Confirm registration success
            registration_result = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )

            if not registration_result:
                self.fail("Registration success message not found")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()