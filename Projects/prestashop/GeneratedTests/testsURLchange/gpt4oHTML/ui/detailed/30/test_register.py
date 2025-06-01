import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check for header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header:
            self.fail("Header is missing")

        # Check for footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer:
            self.fail("Footer is missing")

        # Check for navigation menu
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        if not nav:
            self.fail("Navigation menu is missing")

        # Check for registration form fields
        # Social title radio buttons
        social_title_mr = wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-1")))
        if not social_title_mr:
            self.fail("Social title (Mr) radio button is missing")

        social_title_mrs = wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-2")))
        if not social_title_mrs:
            self.fail("Social title (Mrs) radio button is missing")
        
        # First name
        firstname = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        if not firstname:
            self.fail("First name input is missing")

        # Last name
        lastname = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        if not lastname:
            self.fail("Last name input is missing")

        # Email
        email = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        if not email:
            self.fail("Email input is missing")

        # Password
        password = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        if not password:
            self.fail("Password input is missing")

        # Agree to terms
        terms_checkbox = wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
        if not terms_checkbox:
            self.fail("Terms and conditions checkbox is missing")
        
        # Save button
        save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
        if not save_button:
            self.fail("Save button is missing")

        # Click save button and observe visual change
        save_button.click()
        self.assertTrue(save_button.is_displayed(), "Save button not displaying after click")

if __name__ == '__main__':
    unittest.main()