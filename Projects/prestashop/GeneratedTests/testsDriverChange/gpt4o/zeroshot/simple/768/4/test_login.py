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
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on the "Sign in" link
        sign_in_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Wait for the login page and fill out the form
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_input = driver.find_element(By.ID, "field-password")
        login_button = driver.find_element(By.ID, "submit-login")

        # Enter credentials
        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        # Click the login button
        login_button.click()

        # Confirm successful login by checking for "Sign out" text
        try:
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        except:
            self.fail("Login failed, 'Sign out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()