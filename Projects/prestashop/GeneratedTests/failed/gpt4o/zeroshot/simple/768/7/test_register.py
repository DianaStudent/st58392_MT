from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@example.com'

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click 'Sign in'
        sign_in = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".user-info a[href*='/login']")))
        sign_in.click()

        # Click 'Create one here' to go to registration page
        registration_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create one here")))
        registration_link.click()

        # Fill out the registration form
        email = self.generate_random_email()

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create an account")))
        
        driver.find_element(By.CSS_SELECTOR, "input[name='id_gender'][value='1']").click()  # Mr.
        driver.find_element(By.CSS_SELECTOR, "input[id='field-firstname']").send_keys("Test")
        driver.find_element(By.CSS_SELECTOR, "input[id='field-lastname']").send_keys("User")
        driver.find_element(By.CSS_SELECTOR, "input[id='field-email']").send_keys(email)
        driver.find_element(By.CSS_SELECTOR, "input[id='field-password']").send_keys("test@user1")
        driver.find_element(By.CSS_SELECTOR, "input[name='psgdpr']").click()  # Agree to terms
        driver.find_element(By.CSS_SELECTOR, "input[name='customer_privacy']").click()  # Customer privacy
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Confirm success by checking the "Sign out" link appears
        sign_out = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out")))
        self.assertIsNotNone(sign_out)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()