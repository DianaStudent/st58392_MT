import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_ui_components(self):
        driver = self.driver
        
        # Open the registration page
        driver.get("http://max/register?returnUrl=%2F")
        
        try:
            # Check header elements
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links")))
            
            # Check main content elements
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-body")))
            
            # Check registration form fields
            self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

            # Check footer elements
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-upper")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-lower")))

        except Exception as e:
            self.fail(f"Test failed due to missing UI component: {str(e)}")

if __name__ == "__main__":
    unittest.main()