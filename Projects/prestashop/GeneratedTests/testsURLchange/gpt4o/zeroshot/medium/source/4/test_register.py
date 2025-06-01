import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_registration_process(self):
        driver = self.driver
        wait = self.wait

        # Click the sign-in link
        sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Click the register link
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Fill in the registration form
        gender_radio = wait.until(EC.element_to_be_clickable((By.ID, "field-id_gender-1")))
        gender_radio.click()

        first_name_input = driver.find_element(By.ID, "field-firstname")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, "field-email")
        email_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email_input.send_keys(f"test_{email_suffix}@user.com")

        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("05/31/1990")

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        # Submit the form
        save_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save']")
        save_button.click()

        # Confirm registration success
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        if not sign_out_link or not sign_out_link.is_displayed():
            self.fail("Registration failed or 'Sign out' link not visible.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()