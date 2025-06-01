import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        
        # Click on the "Sign in" link
        try:
            sign_in_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click on Sign in link: {str(e)}")
        
        # Enter email
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            email_input.send_keys("test@user.com")
        except Exception as e:
            self.fail(f"Failed to find or interact with email input: {str(e)}")
        
        # Enter password
        try:
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
            password_input.send_keys("test@user1")
        except Exception as e:
            self.fail(f"Failed to find or interact with password input: {str(e)}")

        # Click "Sign in" button
        try:
            sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click on Sign in button: {str(e)}")
        
        # Confirm success by checking the presence of "Sign out"
        try:
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        except Exception as e:
            self.fail(f"Sign out link not found after login: {str(e)}")
    
    def tearDown(self):
        # Clean up and close the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()