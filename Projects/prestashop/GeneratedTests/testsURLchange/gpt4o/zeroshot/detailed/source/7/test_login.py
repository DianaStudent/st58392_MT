import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Click the login link from the top navigation
        login_link = wait.until(presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info a[href*='login']")))
        login_link.click()

        # Wait for the login page to load
        wait.until(presence_of_element_located((By.ID, "login-form")))

        # Fill in the email and password fields
        email_field = wait.until(presence_of_element_located((By.ID, "field-email")))
        password_field = driver.find_element(By.ID, "field-password")

        if not email_field or not password_field:
            self.fail("Email or password field is missing or not visible")

        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Wait for the redirect after login
        wait.until(presence_of_element_located((By.ID, "header")))

        # Confirm that login was successful
        sign_out_button = wait.until(presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info a.logout")))
        user_info = driver.find_element(By.CSS_SELECTOR, "#_desktop_user_info span.hidden-sm-down")

        if not sign_out_button or not user_info or user_info.text.strip() == "":
            self.fail("Login failed or user info not visible")

        self.assertIn("Sign out", sign_out_button.text)
        self.assertTrue("test user" in user_info.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()