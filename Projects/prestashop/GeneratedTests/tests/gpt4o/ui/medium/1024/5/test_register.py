import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header presence
        header = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'page-header')))
        self.assertIn("Create an account", header.text)

        # Check form fields presence
        input_fields = {
            "Social title": "field-id_gender-1",
            "First name": "field-firstname",
            "Last name": "field-lastname",
            "Email": "field-email",
            "Password": "field-password",
            "Birthdate": "field-birthday",
        }

        for label, field_id in input_fields.items():
            field = wait.until(
                EC.visibility_of_element_located((By.ID, field_id)))
            self.assertTrue(field.is_displayed(), f"{label} input not visible")

        # Check button presence
        save_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))
        self.assertTrue(save_button.is_displayed(), "Save button not visible")

        # Check link presence
        login_link = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Log in instead!")))
        self.assertTrue(login_link.is_displayed(), "Login link not visible")
        
        # Interact with a button or field, such as clicking the 'Save' button
        save_button.click()

        # Verify no errors occur; check for presence of expected notifications or messages
        # In this case, check for a form validation or required field message
        # This part assumes an error message or similar appears
        try:
            error_message = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'form-control-comment')))
            self.assertTrue(error_message.is_displayed(), "Error message not visible")
        except:
            self.fail("Form submission did not yield expected UI update")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()