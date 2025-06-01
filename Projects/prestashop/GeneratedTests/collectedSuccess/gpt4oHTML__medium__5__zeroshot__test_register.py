import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration_process(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click on sign in link in the top menu
        sign_in_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Step 3: Click on the register link on the login page
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Create account")))
        register_link.click()

        # Step 4: Fill in the registration form fields
        # Select gender
        gender_radio_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='field-id_gender-1'] input")))
        gender_radio_btn.click()

        # Fill in first name
        first_name_input = driver.find_element(By.ID, "field-firstname")
        first_name_input.send_keys("Test")

        # Fill in last name
        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        # Fill in dynamic email
        email = f"test_{int(time.time())}@user.com"
        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(email)

        # Fill in password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Fill in birthday
        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("05/31/1970")

        # Step 5: Check required checkboxes
        psg_dpr_checkbox = driver.find_element(By.NAME, "psgdpr")
        psg_dpr_checkbox.click()
        
        customer_privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        customer_privacy_checkbox.click()

        # Step 6: Submit the form
        save_button = driver.find_element(By.CSS_SELECTOR, "button.form-control-submit")
        save_button.click()

        # Step 7: Confirm success by checking for "Sign out" text in the top bar
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        if not sign_out_link or not sign_out_link.is_displayed():
            self.fail("Sign out link is not displayed, registration might have failed.")
        else:
            print("Registration successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()