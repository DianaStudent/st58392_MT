import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Initialize the ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        # 1. Open the home page
        driver.get("http://localhost:8080/en/")
        
        # 2. Click on the login link in the top menu
        try:
            sign_in_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()
        except Exception as e:
            self.fail("Failed to find or click 'Sign in' link, error: %s" % str(e))

        # 3. Wait for the login page to load
        try:
            self.wait.until(EC.title_contains("Log in"))
        except Exception as e:
            self.fail("Login page did not load, error: %s" % str(e))
        
        # 4. Fill in the email and password fields
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        except Exception as e:
            self.fail("Email or Password field not found, error: %s" % str(e))
        
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # 5. Submit the login form
        try:
            submit_button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
            submit_button.click()
        except Exception as e:
            self.fail("Login form submit button not found or not clickable, error: %s" % str(e))

        # 6. Verify that login was successful by checking for the presence of "Sign out" in the top bar
        try:
            sign_out_text = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))).text
            self.assertIn("Sign out", sign_out_text)
        except Exception as e:
            self.fail("Failed to login or 'Sign out' link was not found, error: %s" % str(e))

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()