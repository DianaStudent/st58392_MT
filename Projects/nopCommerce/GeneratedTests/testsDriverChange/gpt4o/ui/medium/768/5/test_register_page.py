import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegisterPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver
        
        # Check header elements
        try:
            header_links = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-links-wrapper")))
            self.assertIsNotNone(header_links, "Header links are missing")
        except:
            self.fail("Header links are not visible")

        # Check form fields
        try:
            gender_male = self.wait.until(EC.visibility_of_element_located((By.ID, "gender-male")))
            gender_female = self.wait.until(EC.visibility_of_element_located((By.ID, "gender-female")))
            first_name = self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            last_name = self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            email = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            
            self.assertIsNotNone(gender_male, "Gender male option is missing")
            self.assertIsNotNone(gender_female, "Gender female option is missing")
            self.assertIsNotNone(first_name, "First name field is missing")
            self.assertIsNotNone(last_name, "Last name field is missing")
            self.assertIsNotNone(email, "Email field is missing")
        except:
            self.fail("Form fields are not visible")

        # Check register button
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
            self.assertIsNotNone(register_button, "Register button is missing")
        except:
            self.fail("Register button is not visible")

        # Interact with button and ensure no errors
        try:
            register_button.click()
            notifications = self.wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))
            self.assertTrue(notifications.is_displayed() == False, "Error notification is visible after clicking register")
        except:
            self.fail("Clicking the register button caused an error in the UI")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()