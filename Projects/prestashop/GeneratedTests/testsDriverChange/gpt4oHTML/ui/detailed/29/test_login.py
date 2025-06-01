from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIProcess(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        try:
            # Ensure that structural elements are visible
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Check that input fields, buttons, and sections are present
            self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            
            # Interact with "Sign in" button
            sign_in_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_button.click()

            # Wait for login form's presence
            self.wait.until(EC.visibility_of_element_located((By.ID, "login-form")))

            # Confirm visibility of login input elements
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))

        except TimeoutException as e:
            # If any required element is missing, fail the test
            self.fail(f"Required UI component missing: {str(e)}")

    def tearDown(self):
        # Tear down the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()