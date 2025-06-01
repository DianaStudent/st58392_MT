import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header not found or not visible")

        # Main Menu
        try:
            menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "main-menu")))
        except:
            self.fail("Main menu not found or not visible")

        # Footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Footer not found or not visible")

        # Login Form
        try:
            login_form = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-register-form")))
        except:
            self.fail("Login form not found or not visible")

        # Input fields
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
        except:
            self.fail("Username or Password input field not found or not visible")

        # Buttons
        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Login']")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        except:
            self.fail("Login button not found or not visible")

        # Interact with UI elements
        try:
            login_button.click()
        except:
            self.fail("Failed to click the login button")

    def tearDown(self):
        # Tear down the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()