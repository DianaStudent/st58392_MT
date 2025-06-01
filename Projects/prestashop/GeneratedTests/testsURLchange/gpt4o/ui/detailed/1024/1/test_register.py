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
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        
        # Header
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Footer
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible")

        # Breadcrumb
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
        except:
            self.fail("Breadcrumb is not visible")

        # Registration form fields
        form_fields = [
            "field-id_gender-1",
            "field-id_gender-2",
            "field-firstname",
            "field-lastname",
            "field-email",
            "field-password",
            "field-birthday"
        ]
        
        for field_id in form_fields:
            try:
                field = self.wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"Form field with ID '{field_id}' is not visible")

        # Checkboxes
        checkboxes = [
            "optin",
            "psgdpr",
            "newsletter",
            "customer_privacy"
        ]

        for checkbox_name in checkboxes:
            try:
                checkbox = self.wait.until(EC.visibility_of_element_located((By.NAME, checkbox_name)))
            except:
                self.fail(f"Checkbox with name '{checkbox_name}' is not visible")

        # Submit button
        try:
            submit_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit")))
        except:
            self.fail("Submit button is not visible")

        # Test interaction: Click submit button
        try:
            submit_button.click()
        except:
            self.fail("Unable to click the submit button")
        
        # After clicking, check for any reaction, e.g. no error message was missed
        # Here you might want to check for a specific success element or message visibility

if __name__ == "__main__":
    unittest.main()