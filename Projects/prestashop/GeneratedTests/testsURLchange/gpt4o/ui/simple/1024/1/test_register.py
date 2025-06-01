import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        # Check page header
        page_header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(page_header, "Page header not found or not visible.")

        # Check form fields
        firstname_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        self.assertIsNotNone(firstname_field, "First name input field not found or not visible.")
        
        lastname_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        self.assertIsNotNone(lastname_field, "Last name input field not found or not visible.")
        
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertIsNotNone(email_field, "Email input field not found or not visible.")
        
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertIsNotNone(password_field, "Password input field not found or not visible.")

        # Check buttons
        save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-footer .btn-primary")))
        self.assertIsNotNone(save_button, "Save button not found or not visible.")

        # Check links
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in instead!")))
        self.assertIsNotNone(login_link, "Login link not found or not visible.")
        
        # Check privacy and terms checkbox
        privacy_checkbox = self.wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
        self.assertIsNotNone(privacy_checkbox, "Privacy checkbox not found or not visible.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()