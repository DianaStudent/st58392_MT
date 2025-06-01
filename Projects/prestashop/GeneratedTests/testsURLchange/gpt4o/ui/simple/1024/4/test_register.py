import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check form fields
        form_fields = {
            "firstname": "field-firstname",
            "lastname": "field-lastname",
            "email": "field-email",
            "password": "field-password",
            "birthday": "field-birthday"
        }

        for field_name, field_id in form_fields.items():
            try:
                field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"{field_name} field is not visible")

        # Check checkboxes
        checkboxes = ["optin", "psgdpr", "newsletter", "customer_privacy"]
        for checkbox in checkboxes:
            try:
                element = wait.until(EC.visibility_of_element_located((By.NAME, checkbox)))
            except:
                self.fail(f"{checkbox} checkbox is not visible")

        # Check submit button
        try:
            submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
        except:
            self.fail("Submit button is not visible")
        
        # Check navigation links
        navigation_links = [
            ("home", "http://localhost:8080/en/"),
            ("clothes", "http://localhost:8080/en/3-clothes"),
            ("accessories", "http://localhost:8080/en/6-accessories"),
            ("art", "http://localhost:8080/en/9-art"),
            ("login", "http://localhost:8080/en/login")
        ]

        for link_text, link_url in navigation_links:
            try:
                link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"a[href='{link_url}']")))
            except:
                self.fail(f"Navigation link for {link_text} is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()