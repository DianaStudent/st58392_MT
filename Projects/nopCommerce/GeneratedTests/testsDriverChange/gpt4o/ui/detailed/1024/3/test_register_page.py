import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")  # Load the registration page
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait
        
        # Check header elements
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo"))), "Header logo is missing")

        # Check navigation links
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page"))), "Home page link is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products"))), "New products link is missing")
        
        # Check registration form elements
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title"))), "Page title is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "FirstName"))), "First name input is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "LastName"))), "Last name input is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "Email"))), "Email input is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "Password"))), "Password input is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword"))), "ConfirmPassword input is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "register-button"))), "Register button is missing")
        
        # Check visibility of footer elements
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-upper"))), "Footer upper is missing")
        
        # Interact with UI elements
        register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
        register_button.click()
        
        # Confirm UI reaction (simulate by checking alert or validation)
        self.assertTrue(wait.until(EC.alert_is_present()), "No alert present after registration attempt")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()