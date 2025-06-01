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

        # Navigate to login page by clicking "My account"
        my_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        my_account_link.click()

        # Ensure the login page loads fully by checking the "Welcome, Please Sign In!" header
        login_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Welcome, Please Sign In!']")))
        if not login_header:
            self.fail("Login page did not load properly.")

        # Fill in email and password
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")
        
        # Click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-button")))
        login_button.click()

        # Verify that the user is logged in by checking if "Log out" button is present
        logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        if not logout_link:
            self.fail("Login failed; 'Log out' button not found.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()