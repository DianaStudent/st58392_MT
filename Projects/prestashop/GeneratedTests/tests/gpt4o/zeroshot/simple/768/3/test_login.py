import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is installed and PATH is set
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver

        # Navigate to login page
        sign_in_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Fill login form
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))

        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        # Submit login form
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
        sign_in_button.click()

        # Confirm success by checking for "Sign out"
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign out")))
        except:
            self.fail("Login failed: 'Sign out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()