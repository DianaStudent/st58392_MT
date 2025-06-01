import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check Header Presence
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Check for Email input field
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertIsNotNone(email_field)

            # Check for Password input field
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertIsNotNone(password_field)

            # Check for Sign In Button
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertIsNotNone(sign_in_button)

            # Check Forgot Password link
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            self.assertIsNotNone(forgot_password_link)
            
            # Check Create Account link
            create_account_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertIsNotNone(create_account_link)

            # Check for Cart icon
            cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            self.assertIsNotNone(cart_icon)

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()