from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    EMAIL = "test@user.com"
    PASSWORD = "test@user1"
    URL = "http://localhost:8080/en/"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the login link in the top menu.
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 3. Wait for the login page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "login-form"))
        )

        # 4. Fill in the email and password fields.
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )

        if email_field and password_field:
            email_field.send_keys(self.EMAIL)
            password_field.send_keys(self.PASSWORD)
        else:
            self.fail("Email or password field not found")

        # 5. Submit the login form.
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "submit-login"))
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 6. Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]"))
        )

        if sign_out_link:
            self.assertEqual("Sign out", sign_out_link.text)
        else:
            self.fail("Sign out link not found after login")

if __name__ == "__main__":
    unittest.main()