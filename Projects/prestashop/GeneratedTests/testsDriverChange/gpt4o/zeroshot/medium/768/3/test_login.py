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
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Click on the login link in the top menu
        login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Wait for the login page to load
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_field = driver.find_element(By.ID, "field-password")

        # Fill in the email and password fields
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Submit the login form
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Verify that login was successful by checking for "Sign out"
        logout_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))

        if not logout_link:
            self.fail("Login was not successful, 'Sign out' link not found.")

        # Check that the "Sign out" text is not empty
        self.assertTrue(logout_link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()