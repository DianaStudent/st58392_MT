import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_login_page_ui_elements(self):
        driver = self.driver

        try:
            # Wait until the title is loaded
            WebDriverWait(driver, 20).until(
                EC.title_contains("Your store. Login")
            )

            # Check the presence and visibility of the email field
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            self.assertTrue(email_field.is_displayed(), "Email field is not visible")

            # Check the presence and visibility of the password field
            password_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Password"))
            )
            self.assertTrue(password_field.is_displayed(), "Password field is not visible")

            # Check the presence and visibility of the login button
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.login-button"))
            )
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            # Check the presence and visibility of the register button
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.register-button"))
            )
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")

            # Check the presence and visibility of the main title
            main_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h1"))
            )
            self.assertIn("Welcome, Please Sign In!", main_title.text, "Main title is not correct or not visible")

            # Check the presence and visibility of the 'Forgot password?' link
            forgot_password = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Forgot password?"))
            )
            self.assertTrue(forgot_password.is_displayed(), "Forgot password link is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()