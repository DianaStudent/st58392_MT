from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUILoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait
        
        # Verify headers, inputs, buttons existence
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
            self.assertEqual(header.text, "Welcome, Please Sign In!")
            
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.assertTrue(email_input.is_displayed())
            
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.assertTrue(password_input.is_displayed())
            
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
            self.assertTrue(login_button.is_displayed())
            
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
            self.assertTrue(register_button.is_displayed())
            
            # Verify form fields and button
            inputs = driver.find_elements(By.CLASS_NAME, "inputs")
            self.assertGreater(len(inputs), 0, "No input fields found")
            
            buttons = driver.find_elements(By.CLASS_NAME, "button-1")
            self.assertGreater(len(buttons), 0, "No buttons found")

        except Exception as e:
            self.fail(f"UI element not found or visible: {str(e)}")
    
    def test_element_interaction(self):
        driver = self.driver
        wait = self.wait

        # Interacting with login button
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))
            login_button.click()
            
            # Check for error message or UI update
            error_span = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "field-validation-valid")))
            self.assertTrue("Please enter your email" in error_span.text)
        
        except Exception as e:
            self.fail(f"Error during interaction with elements: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()