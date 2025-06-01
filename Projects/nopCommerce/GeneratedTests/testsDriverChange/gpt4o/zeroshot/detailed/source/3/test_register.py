import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.fake = Faker()
        self.base_url = "http://max/"
        self.driver.get(self.base_url)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Click the "Register" link in the top navigation
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration form to load
        wait.until(EC.presence_of_element_located((By.ID, "register-button")))

        # Select gender
        gender_female_radio = driver.find_element(By.ID, "gender-female")
        gender_female_radio.click()

        # Fill in required fields
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")
        email = self.fake.email()
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Company").send_keys("TestCorp")
        driver.find_element(By.ID, "Password").send_keys("test11")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

        # Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Wait for the response page or confirmation message to load
        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))

        # Verify that registration succeeded
        if success_message and success_message.text.strip():
            self.assertIn("Your registration completed", success_message.text)
        else:
            self.fail("Registration success message not found or empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()