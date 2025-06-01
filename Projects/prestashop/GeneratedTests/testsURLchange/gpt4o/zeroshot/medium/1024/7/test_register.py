import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page
        wait.until(EC.presence_of_element_located((By.ID, "index")))

        # Step 2: Click on the login link in the top menu
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info .user-info a")))
        login_link.click()

        # Step 3: Click on the register link on the login page
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill in the registration form fields
        gender_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#field-id_gender-1")))
        gender_radio.click()

        first_name_input = driver.find_element(By.ID, "field-firstname")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(f"test_{random.randint(1000, 9999)}@user.com")

        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Step 5: Check required checkboxes
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        # Step 6: Submit the form
        save_button = driver.find_element(By.CSS_SELECTOR, ".form-footer .btn-primary")
        save_button.click()

        # Step 7: Confirm success by checking for the presence of "Sign out" in the top bar
        sign_out_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        if not sign_out_element or not sign_out_element.text.strip():
            self.fail("Sign out link not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()