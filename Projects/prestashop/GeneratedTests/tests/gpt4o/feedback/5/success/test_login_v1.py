import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click the login link from the top navigation
        login_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info a"))
        )
        login_link.click()

        # Wait for the login page to load
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#login-form"))
        )

        # Fill in the email and password fields
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")

        if email_field.is_displayed() and password_field.is_displayed():
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        else:
            self.fail("Email or Password field is not displayed.")

        # Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        if submit_button.is_displayed():
            submit_button.click()
        else:
            self.fail("Submit button is not displayed.")

        # Wait for the redirect after login
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout"))
        )

        # Confirm that login was successful
        sign_out_link = driver.find_element(By.CSS_SELECTOR, "a.logout")
        user_info = driver.find_element(By.CSS_SELECTOR, "a.account span")

        if not sign_out_link or not sign_out_link.is_displayed():
            self.fail("Sign out link is not visible after login.")

        if not user_info or not user_info.is_displayed():
            self.fail("User info is not visible after login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()