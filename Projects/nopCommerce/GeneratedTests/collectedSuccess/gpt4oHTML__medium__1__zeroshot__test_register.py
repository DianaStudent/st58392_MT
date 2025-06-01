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

class RegisterProcessTest(unittest.TestCase):

    def setUp(self):
        # Setup Selenium with Chrome using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual home page URL

    def generate_email(self):
        # Generate a random email for testing
        domain = "example.com"
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return f"{random_string}@{domain}"

    def test_register_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage.
        # Already done in setUp()

        # 2. Click the "Register".
        try:
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            register_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click the Register link: {e}")

        # 3. Wait for the registration page to load.
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']")))
        except Exception as e:
            self.fail(f"The registration page did not load correctly: {e}")

        # 4. Fill all the fields.
        try:
            driver.find_element(By.ID, "gender-female").click()
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            email = self.generate_email()
            driver.find_element(By.ID, "Email").send_keys(email)
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to fill the registration form: {e}")

        # 5. Submit the registration form.
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to submit the registration form: {e}")

        # 6. Verify that a message like "Your registration completed" is shown.
        try:
            result_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result"))).text
            self.assertIn("Your registration completed", result_message)
        except Exception as e:
            self.fail(f"Registration success message not found or not correct: {e}")

    def tearDown(self):
        # Clean up the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()