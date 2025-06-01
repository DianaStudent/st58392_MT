import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Confirm the presence of main headers
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
            self.assertIsNotNone(header, "Header is not present")
        except:
            self.fail("Header is not present or not visible")

        # Check navigation links
        nav_links = ["http://localhost:8080/en/", "http://localhost:8080/en/3-clothes", 
                      "http://localhost:8080/en/6-accessories", "http://localhost:8080/en/9-art", 
                      "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]
        for link in nav_links:
            try:
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"a[href='{link}']")))
            except:
                self.fail(f"Navigation link to {link} is missing or not visible")

        # Confirm presence of form inputs
        form_fields = ["field-firstname", "field-lastname", "field-email", "field-password"]
        for field_id in form_fields:
            try:
                input_field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
                self.assertIsNotNone(input_field, f"{field_id} is not present")
            except:
                self.fail(f"Input field {field_id} is not present or not visible")

        # Confirm presence of buttons
        button_selectors = ["button[data-link-action='save-customer']", "button[data-dismiss='modal']"]
        for button_selector in button_selectors:
            try:
                button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, button_selector)))
                self.assertIsNotNone(button, "Button is not present")
            except:
                self.fail(f"Button {button_selector} is not present or not visible")

        # Interact with a button
        try:
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
            submit_button.click()
            # Check visual update (for example here ensuring no errors in the UI after clicking)
            WebDriverWait(driver, 5).until(EC.staleness_of(submit_button))  # Wait for any potential redirect
        except:
            self.fail("Failed to interact with the submit button or the UI didn't update correctly after interaction")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()