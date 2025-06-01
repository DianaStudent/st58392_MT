import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationPageUITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except Exception as e:
            self.fail("Header is not visible.")

        # Verify register form elements
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        except Exception as e:
            self.fail("One or more form fields are not visible.")
        
        # Verify buttons
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except Exception as e:
            self.fail("Register button is not visible.")
        
        # Verify footer elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except Exception as e:
            self.fail("Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()