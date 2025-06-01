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

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        
        # Wait for the page to load and check for the login link
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
            )
        except:
            self.fail("Login link not found on home page.")
        
        # Click the login link
        login_link.click()

        # Wait for the login page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
        except:
            self.fail("Login page did not load properly.")

        # Input email
        email_input = driver.find_element(By.ID, "Email")
        self.assertTrue(email_input, "Email input field not found.")
        email_input.send_keys("admin@admin.com")

        # Input password
        password_input = driver.find_element(By.ID, "Password")
        self.assertTrue(password_input, "Password input field not found.")
        password_input.send_keys("admin")

        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")
        self.assertTrue(login_button, "Login button not found.")
        login_button.click()

        # Confirm login by checking for the presence of the "Log out" button
        try:
            logout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertTrue(logout_button, "Log out button not found; login may have failed.")
        except:
            self.fail("Login failed. Log out button not found.")

if __name__ == "__main__":
    unittest.main()