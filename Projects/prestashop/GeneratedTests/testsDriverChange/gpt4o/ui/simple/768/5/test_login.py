import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for and check the header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//header[@id='header']"))
            )
            
            # Verify navigation elements
            nav_contact_us = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))
            )
            
            nav_sign_in = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//i[text()='Sign in']"))
            )

            # Verify main content
            login_header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[text()='Log in to your account']"))
            )
            
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            
            password_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "submit-login"))
            )

            forgot_password_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?"))
            )
            
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here"))
            )

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()