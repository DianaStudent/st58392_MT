import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    EMAIL = "test@user.com"
    PASSWORD = "test@user1"
    HOME_URL = "http://localhost:8080/en/"

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.HOME_URL)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Click the login link
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login')]")))
        sign_in_link.click()

        # 2. Fill in the email and password fields
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))

        email_field.send_keys(self.EMAIL)
        password_field.send_keys(self.PASSWORD)

        # 3. Click the submit button
        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-login")))
        submit_button.click()

        # 4. Verify successful login
        sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]")))
        sign_out_text = sign_out_link.text

        account_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'account')]")))
        account_name = account_link.text

        if not sign_out_text:
            self.fail("Sign out link text is empty")

        if not account_name:
            self.fail("Account name is empty")

        self.assertEqual("Sign out", sign_out_text, "Sign out link not found after login")
        self.assertIn("test user", account_name, "Username not found after login")

if __name__ == "__main__":
    unittest.main()