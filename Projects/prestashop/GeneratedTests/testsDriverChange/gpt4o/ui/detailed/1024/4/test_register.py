import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Check visibility of the header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header not visible")

            # Check presence and visibility of form fields and labels
            form_fields = [
                ("field-firstname", "First name"),
                ("field-lastname", "Last name"),
                ("field-email", "Email"),
                ("field-password", "Password"),
                ("field-birthday", "Birthdate"),
                ("field-id_gender-1", "Mr."),
                ("field-id_gender-2", "Mrs."),
            ]

            for field_id, label_text in form_fields:
                element = self.wait.until(EC.visibility_of_element_located((By.ID, field_id)))
                self.assertTrue(element.is_displayed(), f"{label_text} field not visible")

            # Check visibility of checkboxes
            checkboxes_ids = [
                ("field-optin", "Receive offers from our partners"),
                ("field-psgdpr", "Agree to terms and privacy policy"),
                ("field-newsletter", "Sign up for our newsletter"),
                ("field-customer_privacy", "Customer data privacy"),
            ]

            for checkbox_id, checkbox_text in checkboxes_ids:
                checkbox = self.wait.until(EC.visibility_of_element_located((By.NAME, checkbox_id)))
                self.assertTrue(checkbox.is_displayed(), f"{checkbox_text} checkbox not visible")

            # Check visibility of buttons
            submit_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            self.assertTrue(submit_button.is_displayed(), "Submit button not visible")

            # Check visibility of footer
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer not visible")

        except Exception as e:
            self.fail(f"UI element check failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()