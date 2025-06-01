import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.email = "test@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Click the login link
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a"))
        )
        if not sign_in_link:
            self.fail("Sign in link not found")
        sign_in_link.click()

        # 2. Wait for the login page to load
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if not email_field:
            self.fail("Email field not found on login page")

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if not password_field:
            self.fail("Password field not found on login page")

        # 3. Fill in the email and password fields
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        # 4. Click the submit button
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "submit-login"))
        )
        if not submit_button:
            self.fail("Submit button not found on login page")
        submit_button.click()

        # 5. Wait for the redirect after login
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]"))
        )
        if not sign_out_link:
            self.fail("Sign out link not found after login")

        # 6. Confirm that login was successful
        self.assertEqual("Sign out", sign_out_link.text)

        username_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span"))
        )
        if not username_element:
            self.fail("Username element not found after login")
        self.assertTrue(username_element.text)

if __name__ == "__main__":
    unittest.main()