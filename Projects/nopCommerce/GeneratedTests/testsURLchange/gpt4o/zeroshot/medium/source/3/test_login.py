import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the "Login" link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
        if not login_link:
            self.fail("Login link not found")
        login_link.click()

        # Step 2: Wait for the login page to load
        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        if not email_field:
            self.fail("Email input field not found")

        # Step 3: Enter the email and password
        email_field.send_keys("admin@admin.com")

        password_field = driver.find_element(By.ID, "Password")
        if not password_field:
            self.fail("Password input field not found")
        password_field.send_keys("admin")

        # Step 4: Click the login button to submit the form
        login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
        if not login_button:
            self.fail("Login button not found")
        login_button.click()

        # Step 5: Verify the user is logged in by checking the "Log out" button
        logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        if not logout_button:
            self.fail("Logout button not found – login may have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()