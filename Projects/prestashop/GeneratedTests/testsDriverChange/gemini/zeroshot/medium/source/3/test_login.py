import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Click on the login link in the top menu.
        sign_in_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 2. Wait for the login page to load.
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # 3. Fill in the email and password fields.
        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )

        if email_field and password_field:
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        else:
            self.fail("Email or password field not found")

        # 4. Submit the login form.
        submit_button = wait.until(
            EC.element_to_be_clickable((By.ID, "submit-login"))
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 5. Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        sign_out_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
        )

        if sign_out_link:
            self.assertEqual("Sign out", sign_out_link.text)
        else:
            self.fail("Sign out link not found after login")

if __name__ == "__main__":
    unittest.main()