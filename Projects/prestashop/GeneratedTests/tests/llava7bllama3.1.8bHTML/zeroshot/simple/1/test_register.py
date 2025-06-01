import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def test_registration(self):
        # Go to registration page
        self.driver.get("http://your-registration-page.com/")

        # Get all required fields and checkboxes
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-name='username']"))
        )
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-name='email']"))
        )
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-name='password']"))
        )
        terms_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='terms-checkbox']"))
        )

        # Fill all fields
        username_field.send_keys("test_username")
        email_field.send_keys("test_email")
        password_field.send_keys("test_password")

        # Check checkboxes
        terms_checkbox.click()

        # Submit form
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()

        # Check that the text "Sign out" appears
        sign_out_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-name='sign-out']"))
        )
        self.assertIn("Sign out", sign_out_link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()