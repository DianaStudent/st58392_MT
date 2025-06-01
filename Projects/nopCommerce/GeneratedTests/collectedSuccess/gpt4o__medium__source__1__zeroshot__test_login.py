import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver

        # Step 1: Open the home page
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))
        
        # Step 2: Click the "Login" link
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        login_link.click()

        # Step 3: Wait for the login page to load
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-page")))

        # Step 4: Enter the email and password
        email_input = driver.find_element(By.ID, "Email")
        password_input = driver.find_element(By.ID, "Password")
        
        if not email_input or not password_input:
            self.fail("Email or Password input box not found on login page.")

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")
        
        # Step 5: Click the login button to submit the form
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        if not login_button:
            self.fail("Login button not found on login page.")
        
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present
        try:
            logout_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
            if not logout_button:
                self.fail("Log out button not found, login unsuccessful.")
        except:
            self.fail("Log out button not found within the timeout period.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()