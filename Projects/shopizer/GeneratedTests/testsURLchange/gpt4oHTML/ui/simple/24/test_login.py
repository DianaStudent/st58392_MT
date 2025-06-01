import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') # Run in headless mode for testing
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")
    
    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check the logo
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
            
            # Check the header navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            
            # Go to login page
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            account_button.click()
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            login_link.click()
            
            # Check login form fields
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            
            # Check login form buttons
            remember_me_checkbox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
            submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            
            # Check Accept Cookies Button
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        
        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()