from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_login_page_structure(self):
        # Load the login page
        self.driver.get('http://max/login?returnUrl=%2F')

        # Wait for 20 seconds before interacting with elements
        wait = WebDriverWait(self.driver, 20)

        # Ensure header and footer are visible
        try:
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail('Header or Footer is missing')

        # Check for the presence of login form elements
        try:
            wait.until(EC.presence_of_element_located((By.NAME, 'Email')))
            wait.until(EC.presence_of_element_located((By.NAME, 'Password')))
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Forgot your password?')]")))
        except:
            self.fail('Required login form elements are missing')

    def test_login_button_interaction(self):
        # Load the login page
        self.driver.get('http://max/login?returnUrl=%2F')

        # Wait for 20 seconds before interacting with elements
        wait = WebDriverWait(self.driver, 20)

        # Click the 'Sign In' button and check if it's clicked successfully
        try:
            wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
        except:
            self.fail('Failed to click "Sign In" button')

if __name__ == '__main__':
    unittest.main()