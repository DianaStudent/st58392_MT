from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import uuid
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to Register page
        try:
            my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register')))
            my_account_link.click()
        except:
            self.fail("Register link not found")

        # Fill the registration form
        try:
            gender_male = wait.until(EC.element_to_be_clickable((By.ID, 'gender-male')))
            gender_male.click()
            
            first_name = driver.find_element(By.ID, 'FirstName')
            first_name.send_keys('John')

            last_name = driver.find_element(By.ID, 'LastName')
            last_name.send_keys('Doe')

            email = driver.find_element(By.ID, 'Email')
            unique_email = f"{uuid.uuid4()}@example.com"
            email.send_keys(unique_email)

            password = driver.find_element(By.ID, 'Password')
            password.send_keys('test11')

            confirm_password = driver.find_element(By.ID, 'ConfirmPassword')
            confirm_password.send_keys('test11')

            register_button = driver.find_element(By.ID, 'register-button')
            register_button.click()
        except:
            self.fail("Unable to fill registration form")

        # Verify registration success
        try:
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']")))
            self.assertTrue(success_message.is_displayed())
        except:
            self.fail("Registration success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()