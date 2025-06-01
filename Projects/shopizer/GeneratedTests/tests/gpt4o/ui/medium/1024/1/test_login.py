import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check navigation links are present and visible
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except Exception as e:
            self.fail(f"Navigation link not found: {str(e)}")

        # Check form inputs are present and visible
        try:
            login_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
        except Exception as e:
            self.fail(f"Form input not found: {str(e)}")

        # Check buttons are present and visible
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
            cookie_accept_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except Exception as e:
            self.fail(f"Button not found: {str(e)}")
        
        # Interact with elements
        try:
            cookie_accept_button.click()  # Accept cookies
            login_link.click()  # Click login to check redirection
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))  # Validate navigation
        except Exception as e:
            self.fail(f"Error during interaction with elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()