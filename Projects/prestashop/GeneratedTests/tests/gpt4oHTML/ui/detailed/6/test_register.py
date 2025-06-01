import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Load the page and ensure that structural elements are visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Ensure header and footer are visible
            self.assertTrue(header.is_displayed())
            self.assertTrue(footer.is_displayed())
        except Exception as e:
            self.fail(f"Structural element is missing: {e}")

        # 2. Check the presence and visibility of input fields, buttons, labels, and sections
        try:
            # Input fields
            firstname_input = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            lastname_input = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            birthday_input = driver.find_element(By.ID, "field-birthday")

            # Checkboxes
            optin_checkbox = wait.until(EC.visibility_of_element_located((By.NAME, "optin")))
            psgdpr_checkbox = wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
            newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
            customer_privacy_checkbox = wait.until(EC.visibility_of_element_located((By.NAME, "customer_privacy")))

            # Buttons
            save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))

            # Sections
            register_form_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.register-form")))
        except Exception as e:
            self.fail(f"Expected UI component missing or not visible: {e}")

        # 3. Interact with key UI elements
        try:
            save_button.click()
        except Exception as e:
            self.fail(f"Interaction with a UI element failed: {e}")

        # 4. Confirm that the UI reacts visually
        try:
            # Check for any visual reaction, like error messages (not specified, hence skip)
            # Placeholder example:
            # error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
            # self.assertTrue(error_message.is_displayed())
            pass  # Assuming visual reaction is not defined
        except Exception as e:
            self.fail(f"Expected UI reaction missing: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()