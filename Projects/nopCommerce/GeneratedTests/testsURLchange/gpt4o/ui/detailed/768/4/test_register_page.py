import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        # Check form fields and labels
        fields = {
            "FirstName": "First name:",
            "LastName": "Last name:",
            "Email": "Email:",
            "Company": "Company name:",
            "Password": "Password:",
            "ConfirmPassword": "Confirm password:"
        }
        
        for field_id, label_text in fields.items():
            label = wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[@for='{field_id}']")))
            self.assertEqual(label.text, label_text, f"Label text for {field_id} mismatch")
            input_field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            self.assertTrue(input_field.is_displayed(), f"Input field {field_id} is not visible")
        
        # Check buttons
        register_button = wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")
        
        # Interaction
        register_button.click()
        
        # Check visible interaction feedback
        error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "field-validation-error")))
        self.assertTrue(error_message.is_displayed(), "Error message is not visible after interaction")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()