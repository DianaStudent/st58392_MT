import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_user_registration(self):
        driver = self.driver

        # Open the register page
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Register']"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found: {e}")

        # Wait for the registration form to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']"))
            )
        except Exception as e:
            self.fail(f"Registration form did not load: {e}")

        # Fill out the form
        try:
            # Gender
            gender_female = driver.find_element(By.ID, "gender-female")
            gender_female.click()

            # First name
            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("Test")

            # Last name
            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("User")

            # Email - dynamically generate
            email = driver.find_element(By.ID, "Email")
            email.send_keys(f"testuser_{int(time.time())}@example.com")

            # Company
            company = driver.find_element(By.ID, "Company")
            company.send_keys("TestCorp")

            # Password
            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")

            # Confirm Password
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")

            # Register button
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except Exception as e:
            self.fail(f"Form fill-out failed: {e}")

        # Confirm registration success
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and contains(text(), 'Your registration completed')]"))
            )
            message_text = success_message.text
            self.assertIn("Your registration completed", message_text)
        except Exception as e:
            self.fail(f"Registration confirmation failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()