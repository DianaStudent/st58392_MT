from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")
        
        # Step 2: Click on the login link in the top menu
        try:
            sign_in_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='en/login']")))
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Sign in link is not clickable or not found: {str(e)}")
        
        # Step 3: Click on the register link on the login page
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/en/registration']")))
            register_link.click()
        except Exception as e:
            self.fail(f"Register link is not clickable or not found: {str(e)}")
        
        # Step 4: Fill in the registration form fields
        try:
            gender_mr_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='field-id_gender-1']")))
            gender_mr_radio.click()

            first_name_input = driver.find_element(By.ID, "field-firstname")
            last_name_input = driver.find_element(By.ID, "field-lastname")
            email_input = driver.find_element(By.ID, "field-email")
            password_input = driver.find_element(By.ID, "field-password")
            birthday_input = driver.find_element(By.ID, "field-birthday")

            # Fill in the form
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            unique_email = f"test_{int(time.time())}@user.com"
            email_input.send_keys(unique_email)
            password_input.send_keys("test@user1")
            birthday_input.send_keys("01/01/1990")
        except Exception as e:
            self.fail(f"Form input fields are not interactable or not found: {str(e)}")
        
        # Step 5: Check required checkboxes
        try:
            terms_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='psgdpr']")
            customer_privacy_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='customer_privacy']")

            terms_checkbox.click()
            customer_privacy_checkbox.click()
        except Exception as e:
            self.fail(f"Checkboxes are not clickable or not found: {str(e)}")
        
        # Step 6: Submit the form
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
        except Exception as e:
            self.fail(f"Submit button is not clickable or not found: {str(e)}")
        
        # Step 7: Confirm success by checking for the presence of "Sign out" in the top bar
        try:
            sign_out_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='mylogout']")))
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link should be visible after registering.")
        except Exception as e:
            self.fail(f"Sign out link is not present after registration: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()