from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        
    def test_ui_elements(self):
        driver = self.driver

        # Check presence of key UI elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            page_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-title')))
            self.assertTrue(header.is_displayed(), "Header not visible")
            self.assertTrue(page_title.is_displayed(), "Page title not visible")

            # Verify form fields
            first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'FirstName')))
            last_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'LastName')))
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            confirm_password_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'ConfirmPassword')))
            
            self.assertTrue(first_name_field.is_displayed(), "First name input not visible")
            self.assertTrue(last_name_field.is_displayed(), "Last name input not visible")
            self.assertTrue(email_field.is_displayed(), "Email input not visible")
            self.assertTrue(password_field.is_displayed(), "Password input not visible")
            self.assertTrue(confirm_password_field.is_displayed(), "Confirm password input not visible")

            # Verify buttons
            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
            self.assertTrue(register_button.is_displayed(), "Register button not visible")
            
            # Interact with one or two elements
            first_name_field.send_keys("John")
            last_name_field.send_keys("Doe")
            email_field.send_keys("johndoe@example.com")
            password_field.send_keys("password123")
            confirm_password_field.send_keys("password123")
            register_button.click()
            
            # Verify no errors are shown in UI
            # Assuming that if navigation succeeds, the test passes. Adjust as necessary.
            self.assertNotIn("error", driver.page_source.lower(), "Errors found in UI after interaction.")

        except Exception as e:
            self.fail(f"Test failed due to {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()