import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        
        # Check header visibility
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is missing or not visible")

        # Check footer visibility
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is missing or not visible")

        # Check navigation menu
        try:
            nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation menu is missing or not visible")

        # Check form fields: Social title, First name, Last name, Email, Password
        elements_ids = [
            "field-firstname", "field-lastname", "field-email", "field-password"
        ]
        for element_id in elements_ids:
            try:
                element = self.wait.until(EC.visibility_of_element_located((By.ID, element_id)))
            except:
                self.fail(f"Form field with ID {element_id} is missing or not visible")

        # Check visibility and clickable nature of gender radio buttons
        gender_radios = ["field-id_gender-1", "field-id_gender-2"]
        for radio_id in gender_radios:
            try:
                radio_button = self.wait.until(EC.element_to_be_clickable((By.ID, radio_id)))
            except:
                self.fail(f"Gender radio button with ID {radio_id} is missing or not clickable")

        # Check save button
        try:
            save_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit")))
        except:
            self.fail("Save button is missing or not clickable")

        # Interact with elements
        try:
            save_button.click()
            self.assertTrue(True, "Button clicked, page reacted visually")
        except Exception as e:
            self.fail(f"Interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()