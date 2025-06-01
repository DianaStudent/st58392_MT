import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check header, footer, and navigation presence and visibility
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))
        except Exception as e:
            self.fail(f'Failed to find structural elements: {e}')

        # Checking presence of form fields
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        except Exception as e:
            self.fail(f'Failed to find form fields: {e}')

        # Checking presence of buttons
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except Exception as e:
            self.fail(f'Failed to find Register button: {e}')

        # Interact with key UI elements
        try:
            register_button.click()
        except Exception as e:
            self.fail(f'Failed to click Register button: {e}')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()