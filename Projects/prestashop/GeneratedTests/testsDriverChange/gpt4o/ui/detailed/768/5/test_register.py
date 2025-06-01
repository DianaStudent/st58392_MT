import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Check visibility of header
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check visibility of footer
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible")

        # Check visibility of form fields
        form_fields_ids = [
            "field-id_gender-1",
            "field-id_gender-2",
            "field-firstname",
            "field-lastname",
            "field-email",
            "field-password",
            "field-birthday"
        ]

        for field_id in form_fields_ids:
            try:
                self.wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"Form field with ID {field_id} is not visible")

        # Check visibility of labels and buttons
        labels_and_buttons_text = [
            "Create an account",
            "Mr.", "Mrs.",
            "First name",
            "Last name",
            "Email",
            "Password",
            "Birthdate",
            "Receive offers from our partners",
            "I agree to the terms and conditions and the privacy policy",
            "Sign up for our newsletter",
            "Customer data privacy",
            "Save"
        ]

        for text in labels_and_buttons_text:
            try:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))
            except:
                self.fail(f"Label or button with text '{text}' is not visible")

        # Check presence and functionality of main navigation links
        main_links = [
            ("Home", "http://localhost:8080/en/"),
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
            ("Sign in", "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2Fregistration"),
            ("Create account", "http://localhost:8080/en/registration")
        ]

        for link_text, url in main_links:
            try:
                link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertEqual(link.get_attribute('href'), url)
            except:
                self.fail(f"Navigation link '{link_text}' with URL '{url}' is not visible or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()