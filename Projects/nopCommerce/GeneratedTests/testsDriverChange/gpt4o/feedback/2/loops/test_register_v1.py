import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Navigate to registration page
        register_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/customer/info')]"))
        )
        register_link.click()

        # Wait for the registration form to load
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='page registration-page']"))
        )

        # Fill the registration form
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

        # Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Wait for the registration result page
        registration_result_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='result']"))
        )

        # Verify the registration was successful
        self.assertIsNotNone(registration_result_message)
        self.assertIn("Your registration completed", registration_result_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()