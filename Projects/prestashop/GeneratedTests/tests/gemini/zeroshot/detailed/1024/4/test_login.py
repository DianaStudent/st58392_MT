import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.email = "test@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Click the login link
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_in_link_locator)
        )
        sign_in_link.click()

        # 2. Fill in the email and password fields
        email_field_locator = (By.ID, "field-email")
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_field_locator)
        )
        email_field.send_keys(self.email)

        password_field_locator = (By.ID, "field-password")
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(password_field_locator)
        )
        password_field.send_keys(self.password)

        # 3. Click the submit button
        submit_button_locator = (By.ID, "submit-login")
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        submit_button.click()

        # 4. Wait for the redirect and check for successful login
        sign_out_link_locator = (By.XPATH, "//a[contains(@class, 'logout')]")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_out_link_locator)
            )
        except:
            self.fail("Login failed: Sign out link not found.")

        sign_out_link = driver.find_element(*sign_out_link_locator)
        if not sign_out_link:
            self.fail("Login failed: Sign out link is None.")

        sign_out_text = sign_out_link.text
        if not sign_out_text:
            self.fail("Login failed: Sign out text is empty.")

        self.assertEqual("Sign out", sign_out_text, "Login failed: Sign out text mismatch.")

        # Check for username
        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//span[contains(@class, 'hidden-sm-down')]")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(username_locator)
            )
        except:
            self.fail("Login failed: Username not found.")

        username_element = driver.find_element(*username_locator)
        if not username_element:
            self.fail("Login failed: Username element is None.")

        username_text = username_element.text
        if not username_text:
            self.fail("Login failed: Username text is empty.")
        
        self.assertEqual("test user", username_text, "Login failed: Username mismatch.")

if __name__ == "__main__":
    unittest.main()