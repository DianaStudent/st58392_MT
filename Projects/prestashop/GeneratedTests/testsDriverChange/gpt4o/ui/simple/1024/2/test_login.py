import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def tearDown(self):
        self.driver.quit()

    def test_UI_elements_presence_and_visibility(self):
        driver = self.driver

        try:
            # Check that header is present and visible
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )

            # Check that login form is present and visible
            login_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "login-form"))
            )

            # Check that email input is present and visible
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )

            # Check that password input is present and visible
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            # Check that sign in button is present and visible
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "submit-login"))
            )

            # Check that forgot password link is present and visible
            forgot_password_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?"))
            )

            # Check that registration link is present and visible
            registration_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here"))
            )
        
        except Exception as e:
            self.fail(f"An expected UI element is missing or not visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()