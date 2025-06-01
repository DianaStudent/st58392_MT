import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)

    def generate_email(self):
        # Generate a random email suffixed with @test.com
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{random_string}@test.com"

    def test_register(self):
        driver = self.driver
        driver.get("http://example.com/")  # Replace with actual URL

        # Click the "Register" link in the top navigation
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        if register_link is None:
            self.fail("Register link is not present.")

        register_link.click()

        # Wait for the registration form to load and interact with elements
        gender_female_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "gender-female"))
        )
        if gender_female_radio is None:
            self.fail("Gender radio button is not present.")

        gender_female_radio.click()

        # Fill form with required details
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")
        email = self.generate_email()
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Company").send_keys("TestCorp")
        driver.find_element(By.ID, "Password").send_keys("test11")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

        # Submit the registration form
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "register-button"))
        )
        if register_button is None:
            self.fail("Register button is not present.")

        register_button.click()

        # Wait for the response page or confirmation message to load
        confirmation_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".page-body .result"))
        )

        if confirmation_message is None:
            self.fail("Confirmation message is not present.")

        # Verify registration success
        self.assertIn("Your registration completed", confirmation_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()