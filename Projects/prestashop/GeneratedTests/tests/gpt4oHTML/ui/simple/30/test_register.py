import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Check header is present
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible")

        # Check form is present
        try:
            form = self.wait.until(EC.presence_of_element_located((By.ID, "customer-form")))
        except:
            self.fail("Registration form is not present")

        # Check social title, first name, last name, email fields
        required_fields = {
            "social_title": (By.NAME, "id_gender"),
            "firstname": (By.ID, "field-firstname"),
            "lastname": (By.ID, "field-lastname"),
            "email": (By.ID, "field-email")
        }

        for field_name, locator in required_fields.items():
            try:
                field = self.wait.until(EC.visibility_of_element_located(locator))
            except:
                self.fail(f"{field_name} field is not visible")
        
        # Check password field
        try:
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password field is not visible")

        # Check checkboxes
        checkboxes = [
            (By.NAME, "optin"),
            (By.NAME, "psgdpr"),
            (By.NAME, "newsletter"),
            (By.NAME, "customer_privacy"),
        ]
        
        for checkbox_locator in checkboxes:
            try:
                checkbox = self.wait.until(EC.visibility_of_element_located(checkbox_locator))
            except:
                self.fail(f"Checkbox {checkbox_locator} is not visible")

        # Check Save button
        try:
            save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
        except:
            self.fail("Save button is not visible")

        # Check navigation links
        links_to_check = {
            "home": "http://localhost:8080/en/",
            "clothes": "http://localhost:8080/en/3-clothes",
            "accessories": "http://localhost:8080/en/6-accessories",
            "art": "http://localhost:8080/en/9-art",
            "login": "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art",
        }

        for name, url in links_to_check.items():
            try:
                link = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{url}']")))
            except:
                self.fail(f"{name} link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()