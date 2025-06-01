import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")
    
    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on login link
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Click on register link
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Fill in the registration form fields
        gender_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='field-id_gender-1']")))
        gender_label.click()

        first_name_input = wait.until(EC.presence_of_element_located((By.ID, 'field-firstname')))
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, 'field-lastname')
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, 'field-email')
        random_email = f"test_{random.randint(100000, 999999)}@user.com"
        email_input.send_keys(random_email)

        password_input = driver.find_element(By.ID, 'field-password')
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, 'field-birthday')
        birthday_input.send_keys("01/01/1990")

        # Check required checkboxes
        privacy_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, 'customer_privacy')))
        privacy_checkbox.click()

        psgdpr_checkbox = driver.find_element(By.NAME, 'psgdpr')
        psgdpr_checkbox.click()

        # Submit the form
        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()

        # Confirm success by checking for "Sign out"
        sign_out_text = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Sign out')))

        self.assertTrue(sign_out_text.is_displayed(), "Registration failed, 'Sign out' not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()