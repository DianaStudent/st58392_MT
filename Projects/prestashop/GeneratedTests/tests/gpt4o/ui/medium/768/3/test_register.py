from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check if header "Create an account" is present and visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Create an account']")))
        self.assertIsNotNone(header, "Header 'Create an account' is not found or not visible")

        # Check if form fields are present and visible
        form_fields = [
            ("First name", "field-firstname"),
            ("Last name", "field-lastname"),
            ("Email", "field-email"),
            ("Password", "field-password"),
            ("Birthdate", "field-birthday"),
        ]

        for label_text, field_id in form_fields:
            label = wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[text()='{label_text}']")))
            input_field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            self.assertIsNotNone(label, f"Label '{label_text}' is not found or not visible")
            self.assertIsNotNone(input_field, f"Input field '{field_id}' is not found or not visible")

        # Check if buttons are present and visible
        save_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit'][text()='Save']")))
        self.assertIsNotNone(save_button, "Save button is not found or not visible")

        # Check if navigation links are present and visible
        nav_links = [
            ("Home", "http://localhost:8080/en/"),
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
        ]

        for link_text, url in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{url}'][text()='{link_text}']")))
            self.assertIsNotNone(link, f"Link '{link_text}' with href '{url}' is not found or not visible")
        
        # Interact with a button
        save_button.click()

        # Confirm that interactive elements do not cause errors in the UI
        # Example: Check for a validation message after submission
        try:
            alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))
            self.assertIsNotNone(alert, "Alert message did not appear as expected after form submission")
        except Exception as e:
            self.fail(f"Error while interacting with UI elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()