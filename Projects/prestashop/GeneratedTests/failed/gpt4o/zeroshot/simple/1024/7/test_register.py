from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver
        
        # Navigate to the registration page
        sign_in_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a/span[text()='Sign in']"))
        )
        sign_in_element.click()

        create_account_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='No account? Create one here']"))
        )
        create_account_element.click()

        # Fill the registration form
        first_name_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='First name']/following::input[1]"))
        )
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.XPATH, "//label[text()='Last name']/following::input[1]")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following::input[1]")
        email_input.send_keys(f"test_{self.generate_random_string()}@example.com")

        password_input = driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]")
        password_input.send_keys("test@user1")

        # Check the required checkboxes
        psgdpr_checkbox = driver.find_element(By.XPATH, "//input[@name='psgdpr']")
        psgdpr_checkbox.click()

        customer_privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='customer_privacy']")
        customer_privacy_checkbox.click()

        # Submit the registration form
        save_button = driver.find_element(By.XPATH, "//button[text()=' Save ']")
        save_button.click()

        # Confirm success by checking that the text "Sign out" appears
        try:
            sign_out_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'logout')]/span[text()='Sign out']"))
            )
            self.assertTrue(sign_out_element.is_displayed())
        except Exception as e:
            self.fail("Registration failed or 'Sign out' text did not appear")

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def generate_random_string(length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

if __name__ == "__main__":
    unittest.main()