import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class RegisterPageUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        try:
            # Check presence of key elements
            # Header links
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-links')))
            
            # Form fields
            self.wait.until(EC.visibility_of_element_located((By.ID, 'FirstName')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'LastName')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'ConfirmPassword')))
            
            # Register button
            register_button = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'register-button'))
            )
            
            # Check interactions
            register_button.click()
            
            # After clicking register button, check that validation messages appear for required fields
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.field-validation-valid')))

        except Exception as e:
            self.fail(f"Test failed due to missing element or error: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()