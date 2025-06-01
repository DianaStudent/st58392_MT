import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        
        # Verify structural elements are present
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        except Exception as e:
            self.fail(f"Structural elements missing: {str(e)}")

        # Verify input fields
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            repeat_password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            first_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            state_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "stateProvince")))
            country_select = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[name='country']")))
        except Exception as e:
            self.fail(f"Input fields missing: {str(e)}")

        # Verify buttons
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button[type='submit']")))
        except Exception as e:
            self.fail(f"Buttons missing: {str(e)}")

        # Interact with elements
        try:
            register_button.click()
            # Confirm UI reaction (if any error messages appear)
            error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
            for error in error_messages:
                self.assertTrue(error.is_displayed(), "Error message should be displayed")
        except Exception as e:
            self.fail(f"Interaction with elements failed: {str(e)}")
        
    def tearDown(self):
        # Quit the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()