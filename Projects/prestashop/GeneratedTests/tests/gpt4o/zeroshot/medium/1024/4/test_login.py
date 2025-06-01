from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        
        # Step 2: Click on the login link in the top menu
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a/span[contains(text(),'Sign in')]"))
        )
        login_link.click()

        # Step 3: Wait for the login page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Log in to your account')]"))
        )

        # Step 4: Fill in the email and password fields
        email_input = driver.find_element(By.ID, 'field-email')
        password_input = driver.find_element(By.ID, 'field-password')

        if not email_input or not password_input:
            self.fail("Email or password input field not found")

        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        # Step 5: Submit the login form
        submit_button = driver.find_element(By.ID, 'submit-login')

        if not submit_button:
            self.fail("Submit button not found")

        submit_button.click()

        # Step 6: Verify that login was successful by checking for the presence of "Sign out" in the top bar
        try:
            sign_out = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sign out')]"))
            )
        except:
            self.fail("Sign out link not found, login might have failed")

        self.assertIsNotNone(sign_out, "Failed to login, 'Sign out' was not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()