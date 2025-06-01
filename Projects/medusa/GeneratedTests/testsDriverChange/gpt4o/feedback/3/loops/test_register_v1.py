import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8000/dk"

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Step 1: Open the homepage.
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        except Exception as e:
            self.fail("Homepage did not load correctly: " + str(e))
        
        # Step 2: Click the "Account" button in the top right corner.
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
            )
            account_button.click()
        except Exception as e:
            self.fail("Failed to find or click account button: " + str(e))
        
        # Step 3: Click the "Join Us" button below the login form.
        try:
            join_us_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']"))
            )
            join_us_button.click()
        except Exception as e:
            self.fail("Failed to find or click join us button: " + str(e))
        
        # Step 4: Fill in all fields and generate a unique email.
        unique_email = f"user_{int(time.time())}@test.com"
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']"))
            )
            first_name_input.send_keys("user")

            last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
            last_name_input.send_keys("test")

            email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
            email_input.send_keys(unique_email)

            password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail("Failed to fill registration form: " + str(e))
        
        # Step 5: Submit the registration form.
        try:
            register_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
            register_button.click()
        except Exception as e:
            self.fail("Failed to submit registration form: " + str(e))
        
        # Step 6: Verify registration success.
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail("Registration success verification failed: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()