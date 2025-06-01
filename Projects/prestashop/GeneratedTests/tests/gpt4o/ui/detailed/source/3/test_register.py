import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration_page_elements(self):
        driver = self.driver

        # Load the registration page
        driver.get("http://localhost:8080/en/registration")

        # Check for structural elements
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(header, "Header not visible")
        self.assertIsNotNone(footer, "Footer not visible")

        # Check for form field inputs
        inputs = {
            "Social title": "field-id_gender-1",
            "First name": "field-firstname",
            "Last name": "field-lastname",
            "Email": "field-email",
            "Password": "field-password",
            "Birthdate": "field-birthday"
        }

        for label, input_id in inputs.items():
            field = self.wait.until(EC.visibility_of_element_located((By.ID, input_id)))
            self.assertIsNotNone(field, f"{label} input not visible")

        # Check for buttons
        save_button = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button[data-link-action='save-customer']"))
        )
        self.assertIsNotNone(save_button, "Save button not visible")

        # Check for labels and sections
        labels = [
            "Social title", "First name", "Last name", "Email", "Password",
            "Birthdate", "Receive offers from our partners", "I agree to the terms"
        ]
        
        for label_text in labels:
            label = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//label[contains(text(), '{label_text}')]"))
            )
            self.assertIsNotNone(label, f"Label '{label_text}' not visible")

        # Interact with key UI elements
        save_button.click()

        # Confirm UI reacts (this normally involves checking for results after a button click, e.g., alert or new page)
        # Since we don't have explicit UI reactions to test against, we'll consider click is not throwing exceptions as success

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()