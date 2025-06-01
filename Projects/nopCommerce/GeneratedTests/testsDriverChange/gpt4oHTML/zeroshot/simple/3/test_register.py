import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://max/register"
        self.driver.get(self.base_url)

    def generate_random_email(self):
        # Generate a random email address for registration
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

    def test_register_user(self):
        driver = self.driver

        try:
            # Wait for the main registration form to be present
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.XPATH, "//form[@action='/register?returnurl=%2F']")))

            # Fill in the registration fields
            driver.find_element(By.ID, "gender-male").click()  # Select gender
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            driver.find_element(By.ID, "Email").send_keys(self.generate_random_email())
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

            # Click the register button
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Wait for the registration result
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            result_text = driver.find_element(By.CLASS_NAME, "result").text

            # Check if the success message is displayed
            self.assertIn("Your registration completed", result_text)

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()