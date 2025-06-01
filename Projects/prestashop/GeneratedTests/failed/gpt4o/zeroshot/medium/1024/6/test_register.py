from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Click on the Sign in link
        sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible")
        sign_in_link.click()

        # Step 2: Click on the register link
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")
        register_link.click()

        # Step 3: Fill in the registration form fields
        radio_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        radio_mr.click()

        first_name_field = driver.find_element(By.ID, "field-firstname")
        last_name_field = driver.find_element(By.ID, "field-lastname")
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")
        birthday_field = driver.find_element(By.ID, "field-birthday")

        # Generate email
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        
        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        email_field.send_keys(email)
        password_field.send_keys("test@user1")
        birthday_field.send_keys("01/01/1980")

        # Check required checkboxes
        psgdpr_checkbox = driver.find_element(By.NAME, "psgdpr")
        customer_privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        
        psgdpr_checkbox.click()
        customer_privacy_checkbox.click()

        # Step 4: Submit the form
        save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_button.click()
        
        # Step 5: Confirm success by checking for "Sign out"
        sign_out_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out")))
        self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()