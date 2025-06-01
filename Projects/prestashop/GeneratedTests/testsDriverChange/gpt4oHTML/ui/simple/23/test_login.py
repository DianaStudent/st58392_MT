import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_page_elements(self):
        driver = self.driver

        # Navigate to the login page
        login_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']"))
        )
        login_link.click()

        # Check the presence of the Email field
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "field-email"))
        )
        self.assertTrue(email_field.is_displayed(), "Email field is not visible.")

        # Check the presence of the Password field
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "field-password"))
        )
        self.assertTrue(password_field.is_displayed(), "Password field is not visible.")

        # Check the presence of the Sign in button
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "submit-login"))
        )
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible.")

        # Check the presence of the Forgot your password? link
        forgot_password_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?"))
        )
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot your password? link is not visible.")

        # Check the presence of the No account? Create one here link
        create_account_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        self.assertTrue(create_account_link.is_displayed(), "No account? Create one here link is not visible.")

if __name__ == "__main__":
    unittest.main()