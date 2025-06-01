import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        
        # Wait and click on the "Sign in" link
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/en/login']"))
        )
        sign_in_link.click()

        # Wait for login page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#login-form"))
        )

        # Fill in email
        email_field = driver.find_element(By.CSS_SELECTOR, "#field-email")
        if not email_field:
            self.fail("Email field is not present or not visible.")
        email_field.send_keys("test@user.com")

        # Fill in password
        password_field = driver.find_element(By.CSS_SELECTOR, "#field-password")
        if not password_field:
            self.fail("Password field is not present or not visible.")
        password_field.send_keys("test@user1")

        # Click the submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, "button#submit-login")
        if not submit_button:
            self.fail("Submit button is not present or not visible.")
        submit_button.click()

        # Wait for the homepage to load after login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout"))
        )

        # Verify "Sign out" button is present
        sign_out_button = driver.find_element(By.CSS_SELECTOR, "a.logout")
        if not sign_out_button or "Sign out" not in sign_out_button.text:
            self.fail("Sign out button is not present or visible.")

        # Verify that the username is visible in the top navigation
        user_name_display = driver.find_element(By.CSS_SELECTOR, "a.account span.hidden-sm-down")
        if not user_name_display or "test user" not in user_name_display.text:
            self.fail("Username display is not present or incorrect.")

if __name__ == "__main__":
    unittest.main()