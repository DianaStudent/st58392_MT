import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the "Register" link in the top navigation
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Step 2: Wait for the registration form to load
        registration_header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Register", registration_header.text, "Registration page did not load properly.")
        
        # Step 3: Fill in registration details using provided credentials
        gender_female_radio = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        gender_female_radio.click()

        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, "LastName")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, "Email")
        dynamic_email = f"testuser_{int(time.time())}@example.com"
        email_input.send_keys(dynamic_email)

        company_input = driver.find_element(By.ID, "Company")
        company_input.send_keys("TestCorp")

        password_input = driver.find_element(By.ID, "Password")
        password_input.send_keys("test11")

        confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_input.send_keys("test11")

        # Step 4: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Step 5: Wait for the response page or confirmation message to load
        result_text_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))

        # Step 6: Verify registration success by checking confirmation text
        self.assertIn("Your registration completed", result_text_element.text, "Registration was not successful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()