from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
import string


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def generate_email(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "@test.com"

    def test_registration(self):
        driver = self.driver

        # Navigate to "Register" page
        try:
            register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link could not be found or clicked.")

        # Wait for the registration form
        try:
            registration_form = self.wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        except:
            self.fail("Registration form did not load in time.")

        # Fill registration form
        try:
            driver.find_element(By.ID, "gender-female").click()  # Select gender
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            email = self.generate_email()
            driver.find_element(By.ID, "Email").send_keys(email)
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
            driver.find_element(By.ID, "register-button").click()
        except Exception as e:
            self.fail(f"Failed to fill registration form: {e}")

        # Wait for registration confirmation
        try:
            result_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertTrue("Your registration completed" in result_message.text, "Registration success message not found.")
        except:
            self.fail("Registration confirmation did not appear.")

if __name__ == "__main__":
    unittest.main()