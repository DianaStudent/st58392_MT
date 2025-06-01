import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for main UI components
        try:
            # Page Header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Create Account Form
            form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))

            # Social Title Radio Buttons
            radio_mr = wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-1")))
            radio_mrs = wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-2")))

            # First Name Field
            first_name = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))

            # Last Name Field
            last_name = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))

            # Email Field
            email = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))

            # Password Field with minimum length and score requirements
            password = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))

            # Password Strength Feedback
            password_strength = driver.find_element(By.CSS_SELECTOR, ".password-strength-feedback")

            # Birthdate Field
            birthday = wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))

            # Opt-in Checkbox
            optin = driver.find_element(By.NAME, "optin")

            # Terms and Conditions Checkbox
            terms_conditions = wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))

            # Newsletter Checkbox
            newsletter = driver.find_element(By.NAME, "newsletter")

            # Customer Privacy Checkbox
            customer_privacy = wait.until(EC.visibility_of_element_located((By.NAME, "customer_privacy")))

            # Submit Button
            submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-link-action="save-customer"]')))

        except Exception as e:
            self.fail(f"UI component is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()