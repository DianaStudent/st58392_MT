from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page (already done in setUp).

        # Step 2: Click on the login link in the top menu.
        login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a/span[contains(text(),'Sign in')]")))
        self.assertIsNotNone(login_link, "Login link is not present or not visible")
        login_link.click()

        # Step 3: Wait for the login page to load.
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields.
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "field-email")))
        self.assertIsNotNone(email_field, "Email field is not present or not visible")
        email_field.send_keys("test@user.com")

        password_field = wait.until(EC.element_to_be_clickable((By.ID, "field-password")))
        self.assertIsNotNone(password_field, "Password field is not present or not visible")
        password_field.send_keys("test@user1")

        # Step 5: Submit the login form.
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
        self.assertIsNotNone(submit_button, "Submit button is not present or not visible")
        submit_button.click()

        # Step 6: Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        sign_out_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a/span[contains(text(),'Sign out')]")))
        self.assertIsNotNone(sign_out_link, "Sign out link is not present or login failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()