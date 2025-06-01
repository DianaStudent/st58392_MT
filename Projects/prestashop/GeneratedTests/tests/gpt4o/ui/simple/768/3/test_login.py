import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_login_page_ui(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify title
        self.assertEqual(driver.title, "Login", "Title does not match")

        # Verify header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.page-header h1")))
            self.assertIsNotNone(header, "Header is not visible")
        except Exception as e:
            self.fail(f"Header not found: {str(e)}")

        # Verify email field
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertIsNotNone(email_field, "Email field is not visible")
        except Exception as e:
            self.fail(f"Email field not found: {str(e)}")

        # Verify password field
        try:
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertIsNotNone(password_field, "Password field is not visible")
        except Exception as e:
            self.fail(f"Password field not found: {str(e)}")

        # Verify forgot password link
        try:
            forgot_password = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            self.assertIsNotNone(forgot_password, "Forgot password link is not visible")
        except Exception as e:
            self.fail(f"Forgot password link not found: {str(e)}")

        # Verify sign in button
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertIsNotNone(sign_in_button, "Sign in button is not visible")
        except Exception as e:
            self.fail(f"Sign in button not found: {str(e)}")

        # Verify create account link
        try:
            create_account = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertIsNotNone(create_account, "Create account link is not visible")
        except Exception as e:
            self.fail(f"Create account link not found: {str(e)}")

        # Verify cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
            self.assertIsNotNone(cart_icon, "Cart icon is not visible")
        except Exception as e:
            self.fail(f"Cart icon not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()