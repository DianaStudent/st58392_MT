from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class RegistrationPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait
        
        # Elements to be checked
        elements = {
            "header": (By.ID, "header"),
            "footer": (By.ID, "footer"),
            "registration_form": (By.ID, "customer-form"),
            "first_name_label": (By.XPATH, "//label[@for='field-firstname']"),
            "first_name_input": (By.ID, "field-firstname"),
            "last_name_label": (By.XPATH, "//label[@for='field-lastname']"),
            "last_name_input": (By.ID, "field-lastname"),
            "email_label": (By.XPATH, "//label[@for='field-email']"),
            "email_input": (By.ID, "field-email"),
            "password_label": (By.XPATH, "//label[@for='field-password']"),
            "password_input": (By.ID, "field-password"),
            "submit_button": (By.CSS_SELECTOR, "button[data-link-action='save-customer']"),
        }

        # Check presence and visibility
        for el_name, selector in elements.items():
            try:
                element = wait.until(EC.visibility_of_element_located(selector))
                self.assertTrue(element.is_displayed(), f"{el_name} is not visible")
            except Exception as e:
                self.fail(f"Element {el_name} not present or clickable within the time limit: {str(e)}")
        
        # Interact with form elements
        try:
            first_name_input = driver.find_element(*elements["first_name_input"])
            first_name_input.send_keys("John")
            
            last_name_input = driver.find_element(*elements["last_name_input"])
            last_name_input.send_keys("Doe")
            
            email_input = driver.find_element(*elements["email_input"])
            email_input.send_keys("johndoe@example.com")
            
            password_input = driver.find_element(*elements["password_input"])
            password_input.send_keys("SecurePass123")
            
            submit_button = driver.find_element(*elements["submit_button"])
            submit_button.click()

            # Assuming visual/UI feedback on form submission, but without knowing the exact HTML changes, just as an example
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".confirmation-message")))

        except Exception as e:
            self.fail(f"Failed interaction with the form or missing UI feedback: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()