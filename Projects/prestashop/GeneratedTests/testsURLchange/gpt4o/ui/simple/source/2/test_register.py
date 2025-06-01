import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        
        # Check the header
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check the registration form
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
        except:
            self.fail("Registration form is not visible")
        
        # Check the social title radio buttons
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-1")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-2")))
        except:
            self.fail("Social title radio buttons are not visible")

        # Check the first name input
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        except:
            self.fail("First name input is not visible")

        # Check the last name input
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        except:
            self.fail("Last name input is not visible")

        # Check the email input
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Email input is not visible")

        # Check the password input
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password input is not visible")

        # Check the birthdate input
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))
        except:
            self.fail("Birthdate input is not visible")

        # Check the terms and conditions checkbox
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
        except:
            self.fail("Terms and conditions checkbox is not visible")
        
        # Check the newsletter checkbox
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, "newsletter")))
        except:
            self.fail("Newsletter checkbox is not visible")

        # Check the 'Save' button
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
        except:
            self.fail("Save button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()