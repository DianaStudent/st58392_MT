from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Generate a unique email address
        unique_email = f"testuser_{int(time.time())}@example.com"

        # Navigate to registration page
        my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        my_account_link.click()

        # Fill the registration form
        try:
            gender_male = wait.until(EC.presence_of_element_located((By.ID, "gender-male")))
            gender_male.click()

            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("Test")

            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("User")

            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(unique_email)

            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("Test Company")

            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except Exception as e:
            self.fail(f"Registration form elements missing: {str(e)}")
        
        # Confirm success by checking success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your registration completed')]"))
            )
            self.assertTrue(success_message.is_displayed(), "Success message not displayed.")
        except Exception as e:
            self.fail(f"Registration success message not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()