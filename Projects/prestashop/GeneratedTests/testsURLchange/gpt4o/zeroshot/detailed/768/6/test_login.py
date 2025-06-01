import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on the 'Sign in' link
        login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Wait for login page to load
        self.wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Fill in the email and password fields
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_field = driver.find_element(By.ID, "field-password")

        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Confirm that login was successful
        try:
            sign_out_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            user_name = driver.find_element(By.CSS_SELECTOR, "a.account span.hidden-sm-down")
            
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not displayed.")
            self.assertIn("test user", user_name.text, "User name is not displayed correctly.")
        except Exception as e:
            self.fail(f"Login failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()