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
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        driver = self.driver

        # Check the presence of header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.page-header h1")))
        self.assertEqual(header.text, "Create an account", "Header text does not match")

        # Check presence of form fields
        firstname = self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        lastname = self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        email = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        password = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))

        self.assertTrue(firstname.is_displayed(), "Firstname field is not visible")
        self.assertTrue(lastname.is_displayed(), "Lastname field is not visible")
        self.assertTrue(email.is_displayed(), "Email field is not visible")
        self.assertTrue(password.is_displayed(), "Password field is not visible")

        # Check buttons
        save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
        self.assertTrue(save_button.is_displayed(), "Save button is not visible")

        # Check interaction - click save button and verify behavior
        save_button.click()

        # Verify that an element displays some feedback or an error (assuming error message for missing fields is present)
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-footer .form-control-submit")))
        self.assertTrue(error_message.is_displayed(), "Error message not displayed after clicking save")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()