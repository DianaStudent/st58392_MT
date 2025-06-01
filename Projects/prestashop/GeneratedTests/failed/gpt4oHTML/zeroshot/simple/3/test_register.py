from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/registration")

    def test_registration_process(self):
        driver = self.driver
        
        # Fill the registration form
        # Select gender
        try:
            gender_mr = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='field-id_gender-1']/input")))
            gender_mr.click()
        
            # Fill first name
            first_name = driver.find_element(By.XPATH, "//label[@for='field-firstname']/following-sibling::div/input")
            first_name.send_keys("Test")

            # Fill last name
            last_name = driver.find_element(By.XPATH, "//label[@for='field-lastname']/following-sibling::div/input")
            last_name.send_keys("User")
        
            # Fill email with random email
            email_input = driver.find_element(By.XPATH, "//label[@for='field-email']/following-sibling::div/input")
            random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"
            email_input.send_keys(random_email)
        
            # Fill password
            password_input = driver.find_element(By.XPATH, "//label[@for='field-password']/following-sibling::div//input")
            password_input.send_keys("test@user1")

            # Check the partner offers checkbox
            partner_offers_checkbox = driver.find_element(By.XPATH, "//input[@name='optin']")
            partner_offers_checkbox.click()

            # Check terms and conditions
            terms_conditions_checkbox = driver.find_element(By.XPATH, "//input[@name='psgdpr']")
            terms_conditions_checkbox.click()

            # Check sign up for newsletter
            newsletter_checkbox = driver.find_element(By.XPATH, "//input[@name='newsletter']")
            newsletter_checkbox.click()

            # Check customer privacy
            privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='customer_privacy']")
            privacy_checkbox.click()

            # Submit the form
            save_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save']")
            save_button.click()
        
            # Verify that the "Sign out" link is displayed, indicating success
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='logout hidden-sm-down' and contains(text(), 'Sign out')]")))
        
        except Exception as e:
            self.fail(f"Test failed due to exception or missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()