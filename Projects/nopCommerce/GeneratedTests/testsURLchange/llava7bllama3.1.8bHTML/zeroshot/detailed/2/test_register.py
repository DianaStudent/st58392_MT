import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")  # Replace with your homepage URL
        
    def tearDown(self):
        self.driver.quit()
        
    def test_register_user(self):
        # Step 1: Open the homepage.
        pass  # Already done in setUp()

        # Step 2: Click the "Register" link in the top navigation.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))).click()
        
        # Step 3: Wait for the registration form to load.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-button")))
        
        # Step 4: Select the appropriate gender radio input based on the provided data.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='gender' and @value='Female']"))).click()
        
        # Step 5: Fill in all required fields from credentials.
        self.fill_form(
            "first_name", "#register-form input[name='first_name']", "Test"
        )
        self.fill_form(
            "last_name", "#register-form input[name='last_name']", "User"
        )
        self.fill_form(
            "email", "#register-form input[name='email']", self.generate_email()
        )
        self.fill_form(
            "company", "#register-form input[name='company']", "TestCorp"
        )
        self.fill_form(
            "password", "#register-form input[name='password']", "test11"
        )
        self.fill_form(
            "confirm_password", "#register-form input[name='confirm_password']", "test11"
        )
        
        # Step 6: Submit the registration form.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-button"))).click()
        
        # Step 7: Wait for the response page or confirmation message to load.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        
        # Step 8: Verify that registration succeeded by checking the success message.
        self.assertTrue(
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='result']"))).text == "Your registration completed"
        )
        
    def fill_form(self, field_name, locator, value):
        try:
            input_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))
            input_field.clear()
            input_field.send_keys(value)
        except Exception as e:
            self.fail(f"Failed to fill {field_name}: {str(e)}")
            
    def generate_email(self):
        # Simulating email generation for testing purposes
        return "test@example.com"
        
if __name__ == "__main__":
    unittest.main()