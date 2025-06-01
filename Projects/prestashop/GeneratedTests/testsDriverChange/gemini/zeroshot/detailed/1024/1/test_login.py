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
        self.email = "test@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Click the login link
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login')]")))
        if not sign_in_link:
            self.fail("Sign in link not found")
        sign_in_link.click()

        # 2. Fill in the email and password fields
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        if not email_field:
            self.fail("Email field not found")
        email_field.send_keys(self.email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        if not password_field:
            self.fail("Password field not found")
        password_field.send_keys(self.password)

        # 3. Click the submit button
        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-login")))
        if not submit_button:
            self.fail("Submit button not found")
        submit_button.click()

        # 4. Verify successful login
        sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]")))
        if not sign_out_link:
            self.fail("Sign out link not found after login")
        self.assertEqual("Sign out", sign_out_link.text)
        
        username_element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'account')]/span")))
        if not username_element:
            self.fail("Username element not found after login")
        self.assertNotEqual("", username_element.text)

if __name__ == "__main__":
    unittest.main()