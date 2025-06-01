import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except:
            self.fail("Navigation links not found or not visible")

        # Check login form fields
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            submit_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Login form fields not found or not visible")

        # Check forgot password link
        try:
            forgot_password_link = self.wait.until(EC.visibility_of_element_located(
                (By.LINK_TEXT, "Forgot your password?")))
        except:
            self.fail("Forgot password link not found or not visible")

        # Check create account link
        try:
            create_account_link = self.wait.until(EC.visibility_of_element_located(
                (By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("Create account link not found or not visible")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()