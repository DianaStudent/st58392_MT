import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/registration')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Check header
            self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            
            # Check "Create an account" heading
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Create an account"]')))
            
            # Check form fields
            self.wait.until(EC.visibility_of_element_located((By.ID, 'field-firstname')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'field-lastname')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'field-birthday')))
            
            # Check checkbox options
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'optin')))
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'psgdpr')))
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'newsletter')))
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'customer_privacy')))
            
            # Check submit button
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        
        except Exception as e:
            self.fail(f'UI element check failed: {str(e)}')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()