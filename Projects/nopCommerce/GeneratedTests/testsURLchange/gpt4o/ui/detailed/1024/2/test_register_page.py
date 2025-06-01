import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_registration_page_elements(self):
        # Load the registration page
        self.driver.get("http://max/register?returnUrl=%2F")

        # Wait for visibility and check for key structural elements
        try:
            header = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )
            footer = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
            )
            master_content = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "master-wrapper-content"))
            )
        except:
            self.fail("Main structural elements are not visible.")
        
        # Check the presence and visibility of input fields, buttons, labels, and sections
        required_elements = [
            ("id", "FirstName"),
            ("id", "LastName"),
            ("id", "Email"),
            ("id", "Password"),
            ("id", "ConfirmPassword"),
            ("id", "register-button"),
            ("name", "Gender"),
            ("id", "small-search-box-form")
        ]

        for selector, value in required_elements:
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.__getattribute__(By, selector.upper()), value))
                )
            except:
                self.fail(f"Element {value} is not present and visible.")

        # Interact with key UI elements
        # Example: Click on Register button (normally you would enter text into fields first)
        register_button = self.driver.find_element(By.ID, "register-button")
        register_button.click()

        # Confirm that the UI reacts visually (Example: Check for presence of validation messages)
        try:
            validation_errors = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "field-validation-error"))
            )
        except:
            self.fail("Validation errors are not present as expected.")

    def tearDown(self):
        # Cleanup the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()