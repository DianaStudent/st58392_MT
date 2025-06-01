import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        
        try:
            # Check header links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
            
            # Check account setting and cart icon
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.pe-7s-user-female')))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.pe-7s-shopbag')))
            
            # Check login form fields
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'repeatPassword')))
            
            # Check form action buttons
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-box button[type="submit"]')))
            
            # Check footer links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact')))

            # Check cookie consent
            self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))

        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()