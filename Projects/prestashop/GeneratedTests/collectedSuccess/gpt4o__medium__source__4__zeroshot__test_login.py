from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Click on the login link
        try:
            sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()
        except:
            self.fail("Login link is not clickable or not found.")

        # Wait for the login page to load
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Login page did not load properly. Email field not found.")

        # Fill in the email and password fields
        email_field.send_keys("test@user.com")
        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys("test@user1")

        # Submit the login form
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Verify that login was successful by checking for "Sign out"
        try:
            sign_out_text = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertTrue(sign_out_text.text.strip(), "Sign out")
        except:
            self.fail("Login was not successful. 'Sign out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()