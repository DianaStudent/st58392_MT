import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Click the login link from the top navigation
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        login_link.click()

        # Wait for the login page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "login-form"))
        )

        # Fill in the email and password fields
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")

        if not email_field or not password_field:
            self.fail("Email and/or password fields are missing on the login page.")

        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")

        if not submit_button:
            self.fail("Submit button is missing on the login page.")

        submit_button.click()

        # Wait for the redirect after login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )

        # Confirm successful login
        try:
            sign_out_button = driver.find_element(By.LINK_TEXT, "Sign out")
            user_name = driver.find_element(By.XPATH, "//*[contains(text(), 'test user')]")

            if not sign_out_button or not user_name:
                self.fail("Sign out button or user name is missing after login.")

        except:
            self.fail("Login was not successful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()