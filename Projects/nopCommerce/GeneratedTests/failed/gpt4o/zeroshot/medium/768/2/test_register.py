from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_registration(self):
        driver = self.driver
        
        # Step 1: Open the homepage
        home_url = driver.current_url
        self.assertIn("http://max/", home_url)
        
        # Step 2: Click the "Register" link
        register_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()
        
        # Step 3: Wait for the registration page to load
        register_page_title = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']"))
        )
        self.assertTrue(register_page_title, "Registration page did not load properly.")
        
        # Generate a unique email
        email = "user_{}@test.com".format(''.join(random.choices(string.ascii_lowercase + string.digits, k=8)))
        
        # Step 4: Fill all the fields
        driver.find_element(By.ID, 'gender-female').click()
        driver.find_element(By.ID, 'FirstName').send_keys("Test")
        driver.find_element(By.ID, 'LastName').send_keys("User")
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Company').send_keys("TestCorp")
        driver.find_element(By.ID, 'Password').send_keys("test11")
        driver.find_element(By.ID, 'ConfirmPassword').send_keys("test11")
        
        # Step 5: Submit the registration form
        register_button = driver.find_element(By.ID, 'register-button')
        register_button.click()
        
        # Step 6: Verify success message
        success_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']"))
        )
        self.assertTrue(success_message, "Registration success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()