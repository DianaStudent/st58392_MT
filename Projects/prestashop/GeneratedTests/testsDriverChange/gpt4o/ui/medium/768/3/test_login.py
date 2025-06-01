import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check presence of header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check presence of login form
            login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
            self.assertTrue(login_form.is_displayed(), "Login form is not visible")

            # Check presence of email input
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")
            
            # Check presence of password input
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")
            
            # Check presence of Sign in button
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible")

            # Check presence of 'Forgot your password?' link
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            self.assertTrue(forgot_password_link.is_displayed(), "Forgot your password link is not visible")
            
            # Check presence of 'Create one here' link
            create_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertTrue(create_account_link.is_displayed(), "Create one here link is not visible")

            # Interact with 'Sign in' button and check for errors
            sign_in_button.click()
            error_notification = driver.find_element(By.ID, 'notifications')
            self.assertTrue(error_notification.is_displayed(), "Error notification is not displayed after clicking sign in with empty fields")
        
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()