import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify 'Register' title is present and visible
        try:
            register_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Register')]")))
        except:
            self.fail("Register title is not present or visible")

        # Verify 'First name' input field
        try:
            first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
        except:
            self.fail("First name input is not present or visible")

        # Verify 'Last name' input field
        try:
            last_name_input = wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
        except:
            self.fail("Last name input is not present or visible")

        # Verify 'Email' input field
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        except:
            self.fail("Email input is not present or visible")

        # Verify 'Newsletter' checkbox
        try:
            newsletter_checkbox = wait.until(EC.visibility_of_element_located((By.ID, "Newsletter")))
        except:
            self.fail("Newsletter checkbox is not present or visible")

        # Verify 'Password' input field
        try:
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        except:
            self.fail("Password input is not present or visible")

        # Verify 'Confirm password' input field
        try:
            confirm_password_input = wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        except:
            self.fail("Confirm password input is not present or visible")

        # Verify 'Register' button
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except:
            self.fail("Register button is not present or visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()