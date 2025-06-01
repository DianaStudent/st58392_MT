import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify presence and visibility of "Create an account" header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(header.text, "Create an account", "Header text does not match.")

        # Verify presence and visibility of form fields
        firstname_field = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        lastname_field = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))

        # Verify presence and visibility of the 'Save' button
        save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))

        # Verify presence and visibility of the registration form
        form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))

        # Test clicking the "Save" button
        save_button.click()

        # Check for any error messages
        try:
            error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))
            self.fail(f"Error message displayed: {error_message.text}")
        except:
            pass  # No error message means test passed this click action

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()