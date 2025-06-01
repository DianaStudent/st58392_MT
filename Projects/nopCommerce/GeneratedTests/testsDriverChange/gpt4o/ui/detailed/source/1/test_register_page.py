from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class RegisterPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Check structural elements
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            self.assertTrue(header.is_displayed(), "Header is not displayed")
            self.assertTrue(footer.is_displayed(), "Footer is not displayed")

            # Check form elements
            gender_male = wait.until(EC.visibility_of_element_located((By.ID, 'gender-male')))
            first_name = wait.until(EC.visibility_of_element_located((By.ID, 'FirstName')))
            last_name = wait.until(EC.visibility_of_element_located((By.ID, 'LastName')))
            email = wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            password = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            confirm_password = wait.until(EC.visibility_of_element_located((By.ID, 'ConfirmPassword')))
            register_button = wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))

            # Assert form elements visibility
            self.assertTrue(gender_male.is_displayed(), "Gender male radio button is not displayed")
            self.assertTrue(first_name.is_displayed(), "First name input is not displayed")
            self.assertTrue(last_name.is_displayed(), "Last name input is not displayed")
            self.assertTrue(email.is_displayed(), "Email input is not displayed")
            self.assertTrue(password.is_displayed(), "Password input is not displayed")
            self.assertTrue(confirm_password.is_displayed(), "Confirm password input is not displayed")
            self.assertTrue(register_button.is_displayed(), "Register button is not displayed")

            # Interact with buttons
            register_button.click()

        except Exception as e:
            self.fail(f"A required UI element is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()