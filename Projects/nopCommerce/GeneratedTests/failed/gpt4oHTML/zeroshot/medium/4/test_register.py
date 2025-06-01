from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import string

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')  # Replace with actual homepage URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_register(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Click the "Register" link
        try:
            my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'My account')))
            my_account_link.click()
        except:
            self.fail("My account link not found")

        # Step 3: Wait for the registration page to load
        try:
            registration_header = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page registration-page']//h1[text()='Register']")))
            self.assertIsNotNone(registration_header, "Registration page did not load correctly")
        except:
            self.fail("Registration header not found")

        # Step 4: Fill all the fields
        try:
            wait.until(EC.element_to_be_clickable((By.ID, 'gender-female'))).click()
            driver.find_element(By.ID, 'FirstName').send_keys('Test')
            driver.find_element(By.ID, 'LastName').send_keys('User')
            email = 'test' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + '@example.com'
            driver.find_element(By.ID, 'Email').send_keys(email)
            driver.find_element(By.ID, 'Company').send_keys('TestCorp')
            driver.find_element(By.ID, 'Password').send_keys('test11')
            driver.find_element(By.ID, 'ConfirmPassword').send_keys('test11')
        except:
            self.fail("One or more registration fields are not found or cannot be filled")

        # Step 5: Submit the registration form
        try:
            driver.find_element(By.ID, 'register-button').click()
        except:
            self.fail("Register button not found")

        # Step 6: Verify successful registration
        try:
            registration_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result')))
            self.assertIn("Your registration completed", registration_result.text, "Registration result message does not match")
        except:
            self.fail("Registration result message not found or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()