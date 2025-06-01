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

        # Navigate to login page
        nav_login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/customer/info']")))
        if not nav_login_link:
            self.fail("Login link not found in the navigation bar.")
        nav_login_link.click()

        # Ensure the login page is loaded
        login_page_title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome, Please Sign In!')]")))
        if not login_page_title:
            self.fail("Login page did not load correctly.")

        # Fill in login form
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        if not (email_input and password_input):
            self.fail("Email or Password input fields are not found.")

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click login button
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-1 login-button']")))
        if not login_button:
            self.fail("Login button not found.")
        login_button.click()

        # Verify login by checking for the log out button
        logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/logout')]")))
        if not logout_button:
            self.fail("Log out button not found. Login might have failed.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()