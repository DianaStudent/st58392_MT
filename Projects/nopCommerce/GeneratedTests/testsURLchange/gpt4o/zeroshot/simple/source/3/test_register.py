import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to register page
        try:
            my_account_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except TimeoutException:
            self.fail("My account link is not available.")
        
        # Fill registration form
        try:
            gender_male_radio = self.wait.until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            )
            gender_male_radio.click()
            
            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("TestFirstName")
            
            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("TestLastName")
            
            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(f"test_{''.join(random.choices(string.ascii_letters, k=10))}@example.com")
            
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")
            
            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")
            
            register_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()
        except TimeoutException:
            self.fail("A required form input or button was not found.")
        
        # Confirm registration success
        try:
            success_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result']"))
            )
            self.assertEqual(success_message.text, "Your registration completed", "Registration was not successful.")
        except TimeoutException:
            self.fail("Registration success message was not found.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()