import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the homepage
        homepage = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".master-wrapper-page")))
        self.assertTrue(homepage, "Homepage did not load")

        # Step 2: Click the "Register"
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Step 3: Wait for the registration page to load
        registration_page_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title h1")))
        self.assertTrue(registration_page_title.text, "Registration page did not load")

        # Step 4: Fill all the fields
        wait.until(EC.presence_of_element_located((By.ID, "gender-female"))).click()
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")
        
        email = self.generate_random_email()
        driver.find_element(By.ID, "Email").send_keys(email)
        
        driver.find_element(By.ID, "Company").send_keys("TestCorp")
        driver.find_element(By.ID, "Password").send_keys("test11")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Step 6: Verify that a message like "Your registration completed" is shown after successful registration
        registration_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
        self.assertTrue(registration_result.text, "Registration success message is not displayed")
        self.assertIn("Your registration completed", registration_result.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()