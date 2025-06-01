import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def random_email(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@example.com"

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage
        driver.get("http://max/")

        # 2. Click the "Register"
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # 3. Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Register')]")))

        # 4. Fill all the fields
        wait.until(EC.presence_of_element_located((By.ID, "gender-female"))).click()
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")
        driver.find_element(By.ID, "Email").send_keys(self.random_email())
        driver.find_element(By.ID, "Company").send_keys("TestCorp")
        driver.find_element(By.ID, "Password").send_keys("test11")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

        # 5. Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        self.assertTrue(register_button.is_enabled())
        register_button.click()

        # 6. Verify that a message like "Your registration completed" is shown after successful registration
        result_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        self.assertIsNotNone(result_message)
        self.assertIn("Your registration completed", result_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()