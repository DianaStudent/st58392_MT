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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on "My account" to go to login page
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account"))).click()

        # Wait for the login page to load
        self.wait.until(EC.presence_of_element_located((By.ID, "main")))

        # Fill email and password
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_field = driver.find_element(By.ID, "Password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")

        if not email_field or not password_field or not login_button:
            self.fail("Missing login form elements.")

        email_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Click login button
        login_button.click()

        # Verify successful login by checking presence of "Log out" button
        logout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))

        if not logout_button:
            self.fail("Log out button not found, login likely failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()