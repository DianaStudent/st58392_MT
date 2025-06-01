from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # Find the "Register" link and click it
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click the 'Register' link: {e}")

        # Verify that we are on the registration page
        self.assertEqual(driver.current_url, "http://max/register?returnurl=%2F")

        # Generate a random email address
        random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        email = f"{random_string}@example.com"

        # Fill out the registration form
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            ).click()
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            ).send_keys("John")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            ).send_keys("Doe")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            ).send_keys(email)
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            ).send_keys("Example Company")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            ).send_keys("test11")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            ).send_keys("test11")
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            ).click()

        except Exception as e:
            self.fail(f"Could not fill out the registration form: {e}")

        # Verify successful registration
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            ).text
            self.assertEqual(success_message, "Your registration completed")
        except Exception as e:
            self.fail(f"Registration was not successful: {e}")


if __name__ == "__main__":
    unittest.main()