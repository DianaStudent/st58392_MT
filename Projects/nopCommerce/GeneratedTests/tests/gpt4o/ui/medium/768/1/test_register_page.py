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
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration_page_elements(self):
        driver = self.driver

        # Confirm presence of header links
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
        except:
            self.fail("Header links are not visible.")

        # Confirm presence of form fields and buttons
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        except:
            self.fail("Form fields are not visible.")

        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except:
            self.fail("Submit button is not visible.")

        # Interacting with one element: Fill email and verify it's correctly filled
        email_input = driver.find_element(By.ID, "Email")
        email_input.send_keys("test@example.com")
        self.assertEqual(email_input.get_attribute("value"), "test@example.com", "Email input value is incorrect.")

        # Verify page does not result in errors after interaction
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Assuming form validation error for not filled fields will occur
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "field-validation-error")))
        except:
            self.fail("Form validation error messages are not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()