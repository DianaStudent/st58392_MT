import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@example.com"

    def test_register(self):
        driver = self.driver
        wait = self.wait

        # Click the "Register" link
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found or not clickable: {str(e)}")

        # Wait for the registration page to load
        try:
            page_title = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Register')]"))
            )
            self.assertIsNotNone(page_title, "Registration page did not load properly.")
        except Exception as e:
            self.fail(f"Registration page not loaded: {str(e)}")

        # Fill out the registration form
        try:
            wait.until(EC.presence_of_element_located((By.ID, "gender-female"))).click()
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            dynamic_email = self.generate_email()
            driver.find_element(By.ID, "Email").send_keys(dynamic_email)
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to fill the registration form: {str(e)}")

        # Submit the registration form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or not clickable: {str(e)}")

        # Verify registration result
        try:
            registration_success = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Your registration completed')]"))
            )
            self.assertTrue(registration_success, "Registration success message not found")
        except Exception as e:
            self.fail(f"Registration success message not displayed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()