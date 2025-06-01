import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage (already done in setUp)

        # Step 2: Navigate to the Register page
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Step 3: Wait for the registration page to load
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Register')]")))

        # Step 4: Fill all the fields
        wait.until(EC.presence_of_element_located((By.ID, "gender-female"))).click()

        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, "LastName")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, "Email")
        random_email = "test" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@example.com"
        email_input.send_keys(random_email)

        company_input = driver.find_element(By.ID, "Company")
        company_input.send_keys("TestCorp")

        password_input = driver.find_element(By.ID, "Password")
        password_input.send_keys("test11")

        confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_input.send_keys("test11")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Step 6: Verify registration success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Your registration completed')]")))

        if not success_message or not success_message.is_displayed():
            self.fail("Registration success message not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()