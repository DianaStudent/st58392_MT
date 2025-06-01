import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Set up the web driver
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
    
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click the "Sign in" link
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()
        except:
            self.fail("Sign in link not found or not clickable.")
        
        # Enter email
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            email_field.send_keys("test@user.com")
        except:
            self.fail("Email field not found or not interactable.")
        
        # Enter password
        try:
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            password_field.send_keys("test@user1")
        except:
            self.fail("Password field not found or not interactable.")
        
        # Submit the login form
        try:
            submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
            submit_button.click()
        except:
            self.fail("Submit button not found or not clickable.")
        
        # Confirm login was successful
        try:
            sign_out_text = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertTrue(sign_out_text.is_displayed(), "Sign out link not displayed after login.")
        except:
            self.fail("Login failed or 'Sign out' not found.")
    
    def tearDown(self):
        # Tear down the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()