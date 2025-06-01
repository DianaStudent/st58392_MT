from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.driver.maximize_window()

    def test_elements_visibility(self):
        driver = self.driver

        try:
            # Wait and check for the presence and visibility of header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )

            # Wait and check for the presence and visibility of email field
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )

            # Wait and check for the presence and visibility of password field
            password_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            # Wait and check for the presence and visibility of login button
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "submit-login"))
            )

            # Wait and check for the presence and visibility of 'No account?' link
            no_account_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here"))
            )

            # Wait and check for the presence and visibility of 'Forgot your password?' link
            forgot_password_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?"))
            )

        except:
            self.fail("One or more UI elements are missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()