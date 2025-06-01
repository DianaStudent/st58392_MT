from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_registration(self):
        # Navigate to the registration page
        self.driver.get("https://example.com/register")

        # Fill all fields for registration and check checkboxes
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#email")))
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
        
        if not email_input or not password_input:
            self.fail("Email and Password fields are missing")

        email_input.send_keys("test@user1")
        password_input.send_keys("test@user1")

        # Click on the register button
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#register"))).click()

        # Check that "Sign out" appear after successful registration
        sign_out_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        
        if not sign_out_link:
            self.fail("Registration failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()