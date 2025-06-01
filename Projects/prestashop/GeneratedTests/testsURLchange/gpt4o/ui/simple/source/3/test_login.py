import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check for header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Check for login form
            login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
            self.assertIsNotNone(login_form)

            # Check for email input
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertIsNotNone(email_input)

            # Check for password input
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertIsNotNone(password_input)

            # Check for sign in button
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertIsNotNone(sign_in_button)

            # Check for forgot password link
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            self.assertIsNotNone(forgot_password_link)

            # Check for create account link
            create_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertIsNotNone(create_account_link)

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()