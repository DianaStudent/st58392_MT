from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Open homepage and click "Register"
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        self.assertTrue(register_link, "Register link not found")
        register_link.click()

        # Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']")))

        # Fill out the registration form
        gender_female = driver.find_element(By.ID, "gender-female")
        first_name = driver.find_element(By.ID, "FirstName")
        last_name = driver.find_element(By.ID, "LastName")
        email = driver.find_element(By.ID, "Email")
        company = driver.find_element(By.ID, "Company")
        password = driver.find_element(By.ID, "Password")
        confirm_password = driver.find_element(By.ID, "ConfirmPassword")
        register_button = driver.find_element(By.ID, "register-button")

        # Check that elements are present
        elements = [gender_female, first_name, last_name, email, company, password, confirm_password, register_button]
        if not all(elements):
            self.fail("One or more form fields are missing")

        # Fill in fields
        gender_female.click()
        first_name.send_keys("Test")
        last_name.send_keys("User")
        dynamic_email = f"testuser{random.randint(1000,9999)}@example.com"
        email.send_keys(dynamic_email)
        company.send_keys("TestCorp")
        password.send_keys("test11")
        confirm_password.send_keys("test11")
        
        # Submit form
        register_button.click()

        # Verify registration success
        success_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='result' and text()='Your registration completed']")))
        self.assertTrue(success_message, "Registration success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()