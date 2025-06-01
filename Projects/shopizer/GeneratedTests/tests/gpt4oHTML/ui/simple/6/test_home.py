import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_components(self):
        # Open home page
        self.driver.get("http://localhost/")
        
        try:
            # Check header logo
            header_logo = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img"))
            )

            # Check language dropdown
            language_dropdown = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-style span"))
            )
            
            # Check main navigation
            main_navigation = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-menu nav ul"))
            )
            
            # Check Login link
            login_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )
            
            # Check Register link
            register_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
            )
            
            # Check product categories in navigation
            categories = ["Home", "Tables", "Chairs"]
            for category in categories:
                nav_item = self.wait.until(
                    EC.visibility_of_element_located((By.LINK_TEXT, category))
                )
            
            # Check cookie consent banner and Accept button
            cookie_banner = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "CookieConsent"))
            )
            accept_button = self.wait.until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            
            # Check if Subscribe to newsletter elements exist
            subscribe_form = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 input[type='email']"))
            )
            subscribe_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 button"))
            )

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()