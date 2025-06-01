import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://max/login?returnUrl=%2F"
        self.driver.get(self.base_url)

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify structural elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-menu')))
        except:
            self.fail("Header, footer, or navigation is not visible.")

        # Verify form fields and buttons
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
        except:
            self.fail("Input fields or buttons are not visible.")

        # Interact with a UI element and confirm reaction
        login_button = driver.find_element(By.CLASS_NAME, 'login-button')
        login_button.click()
        
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'dialog-notifications-error')))
        except:
            self.fail("Expected visual feedback after interaction is missing.")

        # Assert the presence of some other UI sections
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-title')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'topic-block')))
        except:
            self.fail("Key UI sections are not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()