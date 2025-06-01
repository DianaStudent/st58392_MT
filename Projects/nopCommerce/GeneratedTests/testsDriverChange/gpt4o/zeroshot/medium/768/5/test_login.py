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
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Wait for the "My account" link and click it
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("My account link not found on home page.")

        # Wait for the login page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.title_contains("Welcome, Please Sign In!")
            )
        except:
            self.fail("Login page did not load correctly.")

        # Enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys("admin@admin.com")
        except:
            self.fail("Email input field not found.")

        # Enter password
        try:
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("admin")
        except:
            self.fail("Password input field not found.")

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            login_button.click()
        except:
            self.fail("Login button not found.")

        # Verify the "Log out" button is present to confirm login
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            if not logout_link.is_displayed():
                self.fail("Log out button is not visible.")
        except:
            self.fail("Log out button not found after login.")

if __name__ == "__main__":
    unittest.main()