import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestShopizerUI(unittest.TestCase):
    
    def setUp(self):
        # Setup the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Header elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Footer elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.footer-logo img")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            
            # Login/Register form elements
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[name='country']")))
            wait.until(EC.visibility_of_element_located((By.NAME, "stateProvince")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

        except Exception as e:
            self.fail(f"UI element test failed: {e}")

    def tearDown(self):
        # Teardown and close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()