import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class RegistrationPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/registration")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except Exception:
            self.fail("Header is missing or not visible.")

        # Check footer
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except Exception:
            self.fail("Footer is missing or not visible.")

        # Check form fields
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-1")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-2")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))
            wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
            wait.until(EC.visibility_of_element_located((By.NAME, "customer_privacy")))
        except Exception:
            self.fail("One or more form fields are missing or not visible.")

        # Check buttons
        try:
            save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            save_button.click()  # Interact with the save button
        except Exception:
            self.fail("Save button is missing, not visible or not clickable.")

        # Check 'Create an account' heading
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Create an account']")))
        except Exception:
            self.fail("Create an account heading is missing or not visible.")

        # Confirm UI reacts visually
        try:
            error_messages = driver.find_elements(By.CLASS_NAME, 'form-control-comment')
            self.assertTrue(any([msg.is_displayed() for msg in error_messages]), "Expected an error message, but none displayed.")
        except Exception:
            self.fail("Form submission did not result in UI feedback.")

if __name__ == "__main__":
    unittest.main()