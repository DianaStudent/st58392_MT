import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to registration page
        try:
            my_account_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()

            register_page_title = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            self.assertEqual(register_page_title.text, "Register", "Register page is not loaded.")
        except Exception as e:
            self.fail(f"Failed to navigate to registration page: {e}")

        # Generate a random email
        random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

        # Fill registration form
        try:
            wait.until(EC.presence_of_element_located((By.ID, "gender-male"))).click()
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            driver.find_element(By.ID, "Email").send_keys(random_email)
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
            
            driver.find_element(By.ID, "register-button").click()
        except Exception as e:
            self.fail(f"Failed to fill registration form: {e}")

        # Confirm registration success
        try:
            registration_result = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
            )
            self.assertIn("Your registration completed", registration_result.text, "Registration was not successful.")
        except Exception as e:
            self.fail(f"Failed to confirm registration success: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()