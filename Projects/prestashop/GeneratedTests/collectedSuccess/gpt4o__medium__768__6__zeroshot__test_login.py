import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")

        # Step 2: Click on the login link
        login_link = self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Sign in")
        ))
        login_link.click()

        # Step 3: Wait for the login page to load
        email_field = self.wait.until(EC.presence_of_element_located(
            (By.ID, "field-email")
        ))

        # Check if email field exists
        if not email_field:
            self.fail("Email input field is missing")

        # Step 4: Fill in the email and password fields
        email_field.send_keys("test@user.com")

        password_field = driver.find_element(By.ID, "field-password")

        # Check if password field exists
        if not password_field:
            self.fail("Password input field is missing")

        password_field.send_keys("test@user1")

        # Step 5: Submit the login form
        submit_button = driver.find_element(By.ID, "submit-login")

        # Check if submit button exists
        if not submit_button:
            self.fail("Submit button is missing")

        submit_button.click()

        # Step 6: Verify successful login
        try:
            sign_out = self.wait.until(EC.presence_of_element_located(
                (By.LINK_TEXT, "Sign out")
            ))
        except:
            self.fail("Login failed: 'Sign out' link is not present")

        # Check if sign out text is not empty
        self.assertIsNotNone(sign_out, "Sign out element is empty")

if __name__ == "__main__":
    unittest.main()