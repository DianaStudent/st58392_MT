import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Navigate to registration page
        try:
            register_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/register')]"))
            )
            register_link.click()
        except:
            self.fail("Register link not found or clickable.")

        # Wait for the registration form to load
        try:
            wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='page registration-page']"))
            )
        except:
            self.fail("Registration page did not load.")

        # Fill the registration form
        try:
            gender_female = driver.find_element(By.ID, "gender-female")
            gender_female.click()

            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")

            email_input = driver.find_element(By.ID, "Email")
            generated_email = f"testuser_{int(time.time())}@example.com"
            email_input.send_keys(generated_email)

            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("TestCorp")

            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")
        except:
            self.fail("Failed to fill the registration form.")

        # Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button not found or clickable.")

        # Wait for the registration result page
        try:
            registration_result_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result']"))
            )
        except:
            self.fail("Registration result not found.")

        # Verify the registration was successful
        self.assertIsNotNone(registration_result_message, "Registration result message is None.")
        self.assertIn("Your registration completed", registration_result_message.text, "Registration confirmation text not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()