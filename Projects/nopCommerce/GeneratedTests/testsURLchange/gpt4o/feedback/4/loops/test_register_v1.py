import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver

        # Step 1: Open the homepage
        driver.get("http://max/")

        # Step 2: Click the "Register" link in the top navigation.
        register_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Register')]")))
        register_link.click()

        # Step 3: Wait for the registration form to load.
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Register')]")))

        # Step 4: Select the appropriate gender radio input
        gender_female = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        gender_female.click()

        # Step 5: Fill in all required fields
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        last_name_field = driver.find_element(By.ID, "LastName")
        email_field = driver.find_element(By.ID, "Email")
        company_field = driver.find_element(By.ID, "Company")
        password_field = driver.find_element(By.ID, "Password")
        confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        
        # Generate a random email
        random_email = f"testuser{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}@example.com"
        email_field.send_keys(random_email)

        company_field.send_keys("TestCorp")
        password_field.send_keys("test11")
        confirm_password_field.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        confirmation_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'result') and contains(text(), 'Your registration completed')]")))

        # Step 8: Verify that registration succeeded
        self.assertTrue("Your registration completed" in confirmation_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()