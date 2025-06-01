import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page (Already opened in setUp).

        # Step 2: Click the "Login" button in the top navigation.
        try:
            login_nav_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            login_nav_button.click()
        except Exception:
            self.fail("Login navigation button not found or clickable")
        
        # Step 3: Wait until the login page loads fully.
        try:
            page_title = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome, Please Sign In!']"))
            )
        except Exception:
            self.fail("Login page did not load successfully")

        # Step 4: Fill in the email and password fields using the provided credentials.
        try:
            email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            password_input = driver.find_element(By.ID, "Password")

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception:
            self.fail("Email or password input fields not found")

        # Step 5: Click the login button.
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
            login_button.click()
        except Exception:
            self.fail("Login button not found or not clickable")

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        except Exception:
            self.fail("Log out button not found after login attempt")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()