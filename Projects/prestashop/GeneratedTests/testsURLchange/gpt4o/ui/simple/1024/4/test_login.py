import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login_page_elements(self):
        try:
            # Check header
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.page-header h1")))
            self.assertTrue(header.is_displayed(), "Header is not displayed")

            # Check email input
            email_input = self.driver.find_element(By.ID, "field-email")
            self.assertTrue(email_input.is_displayed(), "Email input field is not displayed")

            # Check password input
            password_input = self.driver.find_element(By.ID, "field-password")
            self.assertTrue(password_input.is_displayed(), "Password input field is not displayed")

            # Check forgot password link
            forgot_password_link = self.driver.find_element(By.CSS_SELECTOR, ".forgot-password a")
            self.assertTrue(forgot_password_link.is_displayed(), "Forgot password link is not displayed")

            # Check sign in button
            sign_in_button = self.driver.find_element(By.ID, "submit-login")
            self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not displayed")

            # Check create account link
            create_account_link = self.driver.find_element(By.CSS_SELECTOR, ".no-account a")
            self.assertTrue(create_account_link.is_displayed(), "Create account link is not displayed")

        except Exception as e:
            self.fail(f"An expected element is missing or not visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()