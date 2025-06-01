import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Check header components
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-upper")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-lower")))
            
            # Check header links
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-register")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-login")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-wishlist")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-cart")))
            
            # Check the registration form elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".registration-page")))
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
            
            # Check buttons
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

            # Check for footer elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))

        except Exception as e:
            self.fail(f"UI element missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()