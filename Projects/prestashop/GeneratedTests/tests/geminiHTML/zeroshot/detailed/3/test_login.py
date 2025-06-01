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
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        try:
            sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the sign-in link: {e}")

        # 3. Wait for the login page to load.
        try:
            login_form = wait.until(EC.presence_of_element_located((By.ID, "login-form")))
        except Exception as e:
            self.fail(f"Login form did not load: {e}")

        # 4. Fill in the email and password fields using test credentials provided.
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
            email_field.send_keys(self.email)
            password_field.send_keys(self.password)
        except Exception as e:
            self.fail(f"Could not find or fill email/password fields: {e}")

        # 5. Click the submit button.
        try:
            submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-login")))
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the submit button: {e}")

        # 6. Wait for the redirect after login.
        # Waiting for the "Sign out" link to appear, indicating successful login.
        try:
            sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        except Exception as e:
            self.fail(f"Sign out link did not appear after login: {e}")

        # 7. Confirm that login was successful
        #   - The "Sign out" button is present in the top navigation
        #   - The username (e.g. "test user") is also visible in the top navigation.
        try:
            sign_out_text = sign_out_link.text
            self.assertEqual(sign_out_text, "Sign out", "Sign out link text is incorrect")
        except Exception as e:
            self.fail(f"Could not get or verify text of Sign out link: {e}")

        try:
            username_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//span[contains(@class, 'hidden-sm-down')]")))
            username_text = username_element.text
            self.assertTrue(username_text != "", "Username text is empty")
        except Exception as e:
            self.fail(f"Could not get or verify username text: {e}")

if __name__ == "__main__":
    unittest.main()