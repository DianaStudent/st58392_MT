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
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # 1. Open the home page.
        # 2. Click on the login link in the top menu.
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
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
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        else:
            self.fail("Email or password field not found")

        # 5. Submit the login form.
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "submit-login"))
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 6. Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
        )

        if sign_out_link:
            sign_out_text = sign_out_link.text
            if sign_out_text and "Sign out" in sign_out_text:
                pass
            else:
                self.fail("Sign out text not found")
        else:
            self.fail("Sign out link not found")

if __name__ == "__main__":
    unittest.main()