import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on Sign in link
        try:
            sign_in_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except:
            self.fail("Sign in link not found or clickable")

        # Fill in the login form
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            password_input = driver.find_element(By.ID, "field-password")
            email_input.send_keys("test@user.com")
            password_input.send_keys("test@user1")
        except:
            self.fail("Email or Password input field not found")

        # Click submit button
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except:
            self.fail("Submit button not found")

        # Verify login success
        try:
            self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except:
            self.fail("Login failed, 'Sign out' link not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()