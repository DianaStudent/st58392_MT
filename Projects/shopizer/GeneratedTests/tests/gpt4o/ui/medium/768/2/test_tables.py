import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        try:
            # Wait and check for navigation links
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
            
            # Check the login and register links
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
            
            # Interact with the accept cookies button
            accept_cookies_button = driver.find_element(By.ID, 'rcc-confirm-button')
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
            accept_cookies_button.click()
            
            # Verify the CookieConsent should disappear
            WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'CookieConsent')))
        
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
    
    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()