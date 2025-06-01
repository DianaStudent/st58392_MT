import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not displayed")

        # Check 'Create an account' heading
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.page-header h1")))
        except:
            self.fail("'Create an account' heading is not displayed")

        # Check form fields
        form_fields = [
            "field-id_gender-1", "field-id_gender-2",
            "field-firstname", "field-lastname", 
            "field-email", "field-password", 
            "field-birthday"
        ]
        for field in form_fields:
            try:
                wait.until(EC.visibility_of_element_located((By.ID, field)))
            except:
                self.fail(f"Form field with ID '{field}' is not displayed")
        
        # Check select inputs and checkboxes
        checkboxes = [
            "optin", "psgdpr", "newsletter", "customer_privacy"
        ]
        for checkbox in checkboxes:
            try:
                wait.until(EC.visibility_of_element_located((By.NAME, checkbox)))
            except:
                self.fail(f"Checkbox with name '{checkbox}' is not displayed")

        # Check 'Save' button
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
        except:
            self.fail("Save button is not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()