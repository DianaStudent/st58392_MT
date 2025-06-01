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
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the login link in the top menu.
        try:
            sign_in_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. Wait for the login page to load.
        try:
            wait.until(
                EC.presence_of_element_located((By.ID, "login-form"))
            )
        except Exception as e:
            self.fail(f"Login form did not load: {e}")

        # 4. Fill in the email and password fields.
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )

            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")

        except Exception as e:
            self.fail(f"Could not find or fill email/password fields: {e}")

        # 5. Submit the login form.
        try:
            submit_button = wait.until(
                EC.element_to_be_clickable((By.ID, "submit-login"))
            )
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not find or click submit button: {e}")

        # 6. Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]"))
            )

            if sign_out_link:
                sign_out_text = sign_out_link.text
                if sign_out_text and "Sign out" in sign_out_text:
                    pass  # Login successful
                else:
                    self.fail("Sign out link text is incorrect or empty.")
            else:
                self.fail("Sign out link not found after login.")

        except Exception as e:
            self.fail(f"Login verification failed: {e}")


if __name__ == "__main__":
    unittest.main()