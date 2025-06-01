from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver

        # Step 2: Click on the login link in the top menu
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            login_link.click()
            
            # Step 3: Wait for the login page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "login-form"))
            )
        except:
            self.fail("Login link or form not found")

        # Step 4: Fill in the email and password fields
        try:
            email_field = driver.find_element(By.ID, "field-email")
            password_field = driver.find_element(By.ID, "field-password")
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        except:
            self.fail("Email or password field not found")

        # Step 5: Submit the login form
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except:
            self.fail("Submit button not found")

        # Step 6: Verify successful login
        try:
            WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.LINK_TEXT, "Sign out"), "Sign out")
            )
        except:
            self.fail("Login was not successful, 'Sign out' not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()