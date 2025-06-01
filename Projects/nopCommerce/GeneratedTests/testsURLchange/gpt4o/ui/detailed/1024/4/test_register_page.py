import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegisterPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver

        # Check the visibility of structural elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
        except Exception as e:
            self.fail(f"Structural element missing: {e}")

        # Check the visibility of input fields and labels in registration form
        try:
            form_inputs = [
                (By.ID, 'FirstName'),
                (By.ID, 'LastName'),
                (By.ID, 'Email'),
                (By.ID, 'Password'),
                (By.ID, 'ConfirmPassword'),
                (By.ID, 'Company'),
            ]
            for selector in form_inputs:
                element = self.wait.until(EC.visibility_of_element_located(selector))
            
            gender_label = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@for='gender']")))
            newsletter_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, 'Newsletter')))
            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
        except Exception as e:
            self.fail(f"Input field or label missing: {e}")

        # Interact with registrer button to confirm the page reacts
        try:
            register_button.click()
            # Check for some change in the UI post interaction if applicable
        except Exception as e:
            self.fail(f"Button interaction failed: {e}")

        # All checks complete
        print("All UI elements are present and interactable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()