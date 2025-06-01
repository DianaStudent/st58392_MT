import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPageElements(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check that header is present and visible
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Check login form fields
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertIsNotNone(email_field)

            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertIsNotNone(password_field)

            # Check Sign in button
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertIsNotNone(sign_in_button)

            # Check Forgot your password link
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            self.assertIsNotNone(forgot_password_link)

            # Check No account? Create one here link
            create_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertIsNotNone(create_account_link)

            # Check top menu links
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            self.assertIsNotNone(clothes_link)

            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            self.assertIsNotNone(accessories_link)

            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            self.assertIsNotNone(art_link)

        except Exception as e:
            self.fail(f"Failed due to missing UI component: {e}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()