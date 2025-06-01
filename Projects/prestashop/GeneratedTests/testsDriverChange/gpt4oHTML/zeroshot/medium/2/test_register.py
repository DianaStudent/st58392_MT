import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Verify home page is loaded by checking 'Sign in' link
        sign_in_link = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//header//span[contains(text(), 'Sign in')]")))
        self.assertTrue(sign_in_link)

        # Step 2: Click on 'Sign in' link
        sign_in_link.click()

        # Step 3: Verify login page is loaded by checking 'Log in to your account' header
        login_header = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Log in to your account')]")))
        self.assertTrue(login_header)

        # Step 3: Click on 'Create account' link
        register_link = driver.find_element(By.LINK_TEXT, 'No account? Create one here')
        register_link.click()

        # Step 4: Verify registration page is loaded by checking 'Create an account' header
        register_header = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Create an account')]")))
        self.assertTrue(register_header)

        # Step 5: Fill in the registration form.
        # Select 'Mr.' for gender
        gender_radio = driver.find_element(By.XPATH, "//input[@id='field-id_gender-1']")
        gender_radio.click()

        # Fill in the first name
        first_name = driver.find_element(By.ID, "field-firstname")
        first_name.send_keys("Test")

        # Fill in the last name
        last_name = driver.find_element(By.ID, "field-lastname")
        last_name.send_keys("User")

        # Generate a unique email address
        unique_id = random.randint(100000, 999999)
        email = f"test_{unique_id}@user.com"
        
        # Fill in the email
        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(email)

        # Fill in the password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Fill in the birthdate
        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/1990")

        # Check required checkboxes
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        # Step 6: Submit the form
        save_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()=' Save ']")
        save_button.click()

        # Step 7: Confirm success
        sign_out_link = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//header//span[contains(text(), 'Sign out')]")))
        self.assertTrue(sign_out_link, "Registration failed - 'Sign out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()