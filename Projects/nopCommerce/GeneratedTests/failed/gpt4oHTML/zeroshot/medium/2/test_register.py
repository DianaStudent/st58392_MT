from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegisterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@example.com"
    
    def test_register(self):
        driver = self.driver
        
        # Open the homepage
        driver.get("http://max/")
        
        # Click the "Register"
        header_menu = self.get_element(driver, By.CLASS_NAME, "header-menu")
        register_link = self.get_element(header_menu, By.LINK_TEXT, "Register")
        register_link.click()
        
        # Wait for the registration page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
        )
        
        # Fill all the fields
        self.fill_form(driver)
        
        # Submit the registration form
        register_button = self.get_element(driver, By.ID, "register-button")
        register_button.click()
        
        # Verify that a message like "Your registration completed" is shown after successful registration
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
        )
        
        registration_result = self.get_element(driver, By.CLASS_NAME, "result")
        if registration_result and registration_result.text == "Your registration completed":
            print("Registration successful.")
        else:
            self.fail("Registration result message not found or incorrect.")
        
    def fill_form(self, driver):
        female_radio = self.get_element(driver, By.ID, "gender-female")
        female_radio.click()
        
        firstname_input = self.get_element(driver, By.ID, "FirstName")
        firstname_input.send_keys("Test")
        
        lastname_input = self.get_element(driver, By.ID, "LastName")
        lastname_input.send_keys("User")
        
        email_input = self.get_element(driver, By.ID, "Email")
        email_input.send_keys(self.generate_random_email())
        
        company_input = self.get_element(driver, By.ID, "Company")
        company_input.send_keys("TestCorp")
        
        password_input = self.get_element(driver, By.ID, "Password")
        password_input.send_keys("test11")
        
        confirm_password_input = self.get_element(driver, By.ID, "ConfirmPassword")
        confirm_password_input.send_keys("test11")
    
    def get_element(self, base, by, value):
        try:
            element = WebDriverWait(base, 20).until(
                EC.presence_of_element_located((by, value))
            )
            if element and element.text.strip() != "":
                return element
            else:
                self.fail(f"Element located by {by}='{value}' is empty or missing.")
        except:
            self.fail(f"Element located by {by}='{value}' not found.")
        return None
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()