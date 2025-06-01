import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Check Header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible on the page.")

        # Check Main Header Text
        try:
            main_header_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-header h1")))
        except:
            self.fail("Main header text 'Create an account' is not visible on the page.")

        # Check Form Fields
        form_fields_ids = ["field-id_gender-1", "field-id_gender-2", "field-firstname", "field-lastname", "field-email", "field-password", "field-birthday"]
        for field_id in form_fields_ids:
            try:
                field = self.wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"Form field with ID {field_id} is not visible on the page.")

        # Check Checkboxes
        checkbox_names = ["optin", "psgdpr", "newsletter", "customer_privacy"]
        for name in checkbox_names:
            try:
                checkbox = self.wait.until(EC.visibility_of_element_located((By.NAME, name)))
            except:
                self.fail(f"Checkbox with name {name} is not visible on the page.")

        # Check Submit Button
        try:
            submit_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control-submit")))
        except:
            self.fail("Submit button is not visible on the page.")
        
        # Check Footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer is not visible on the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()