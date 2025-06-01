import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header links
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-wishlist")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-cart")))
        except Exception as e:
            self.fail(f"Header link element not found or not visible: {str(e)}")

        # Verify main sections
        try:
            # Header logo
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))

            # Search box
            wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))

            # Registration form fields
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
            
            # Newsletter checkbox
            wait.until(EC.visibility_of_element_located((By.ID, "Newsletter")))

            # Register button
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        
        except Exception as e:
            self.fail(f"Main section element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()