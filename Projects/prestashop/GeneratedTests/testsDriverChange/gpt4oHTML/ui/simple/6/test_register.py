from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components_exist(self):
        driver = self.driver
        wait = self.wait

        # Check for header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not displayed")
        except:
            self.fail("Header is not found")

        # Check for form
        try:
            form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
            self.assertTrue(form.is_displayed(), "Form is not displayed")
        except:
            self.fail("Form is not found")

        # Check input fields
        fields = [
            "field-firstname",
            "field-lastname",
            "field-email",
            "field-password"
        ]

        for field_id in fields:
            try:
                field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
                self.assertTrue(field.is_displayed(), f"{field_id} field is not displayed")
            except:
                self.fail(f"{field_id} field is not found")

        # Check for buttons and links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in instead!")))
            self.assertTrue(login_link.is_displayed(), "Log in link is not displayed")
        except:
            self.fail("Log in link is not found")

        try:
            save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
            self.assertTrue(save_button.is_displayed(), "Save button is not displayed")
        except:
            self.fail("Save button is not found")

        # Check radio buttons
        radio_buttons = [
            "field-id_gender-1",
            "field-id_gender-2"
        ]

        for radio_id in radio_buttons:
            try:
                radio = wait.until(EC.visibility_of_element_located((By.ID, radio_id)))
                self.assertTrue(radio.is_displayed(), f"{radio_id} radio button is not displayed")
            except:
                self.fail(f"{radio_id} radio button is not found")

        # Check checkboxes
        checkboxes = [
            "field-optin",
            "field-psgdpr",
            "field-newsletter",
            "field-customer_privacy"
        ]

        for checkbox_id in checkboxes:
            try:
                checkbox = wait.until(EC.visibility_of_element_located((By.NAME, checkbox_id)))
                self.assertTrue(checkbox.is_displayed(), f"{checkbox_id} checkbox is not displayed")
            except:
                self.fail(f"{checkbox_id} checkbox is not found")

if __name__ == "__main__":
    unittest.main()