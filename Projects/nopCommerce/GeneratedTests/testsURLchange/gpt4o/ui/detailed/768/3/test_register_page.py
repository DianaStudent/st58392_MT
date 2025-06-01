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
    
    def test_check_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check structural elements
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-menu')))
            
            # Check form fields and buttons
            gender_label = driver.find_element(By.LABEL, 'Gender:')
            first_name_input = driver.find_element(By.ID, 'FirstName')
            last_name_input = driver.find_element(By.ID, 'LastName')
            email_input = driver.find_element(By.ID, 'Email')
            password_input = driver.find_element(By.ID, 'Password')
            confirm_password_input = driver.find_element(By.ID, 'ConfirmPassword')
            register_button = driver.find_element(By.ID, 'register-button')
            
            # Interact with elements
            gender_male = driver.find_element(By.ID, 'gender-male')
            gender_male.click()
            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")
            email_input.send_keys("john.doe@example.com")
            password_input.send_keys("password123")
            confirm_password_input.send_keys("password123")
            register_button.click()
            
            # Confirm interaction and that elements exist
            self.assertTrue(header.is_displayed(), "Header is not visible")
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
            self.assertTrue(navigation.is_displayed(), "Navigation is not visible")
            self.assertTrue(gender_label.is_displayed(), "Gender label is missing or not visible")
            self.assertTrue(first_name_input.is_displayed(), "First name input is missing or not visible")
            self.assertTrue(last_name_input.is_displayed(), "Last name input is missing or not visible")
            self.assertTrue(email_input.is_displayed(), "Email input is missing or not visible")
            self.assertTrue(password_input.is_displayed(), "Password input is missing or not visible")
            self.assertTrue(confirm_password_input.is_displayed(), "Confirm password input is missing or not visible")
            self.assertTrue(register_button.is_displayed(), "Register button is missing or not visible")
        
        except Exception as e:
            self.fail(f"A required UI element is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()