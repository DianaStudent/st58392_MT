import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Click on the login link in the top menu
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Fill in the email and password fields
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")

        if email_field and password_field:
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        else:
            self.fail("Email or Password field is not present.")

        # Submit the login form
        submit_button = driver.find_element(By.ID, "submit-login")
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button is not present.")

        # Verify that login was successful
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        if not sign_out_link:
            self.fail("Sign out link is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()