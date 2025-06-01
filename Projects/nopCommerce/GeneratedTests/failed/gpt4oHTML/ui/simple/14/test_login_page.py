from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver

        # Check for header components
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except:
            self.fail("Header not found or not visible")

        # Check for login elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-login')))
        except:
            self.fail("Login link not found or not visible")

        driver.find_element(By.CLASS_NAME, 'ico-login').click()

        # Detailed checks for the login page
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-page')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
        except:
            self.fail("One or more login page components not found or not visible")

        # Navigate to register page
        driver.get("http://max/register?returnUrl=%2F")

        # Check for registration elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-block')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
        except:
            self.fail("One or more registration page components not found or not visible")

        # Navigate to search page
        driver.get("http://max/search")

        # Check for search box
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
        except:
            self.fail("Search components not found or not visible")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()