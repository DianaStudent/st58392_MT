import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.base_url = 'http://max/'

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get(self.base_url)

        # Step 2: Click the "Register" link in the top navigation
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Step 3: Wait for the registration form to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page.registration-page")))

        # Step 4: Select the appropriate gender radio input based on the provided data
        gender_female = driver.find_element(By.ID, "gender-female")
        gender_female.click()

        # Step 5: Fill in all required fields
        first_name_field = driver.find_element(By.ID, "FirstName")
        last_name_field = driver.find_element(By.ID, "LastName")
        email_field = driver.find_element(By.ID, "Email")
        company_field = driver.find_element(By.ID, "Company")
        password_field = driver.find_element(By.ID, "Password")
        confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        
        # Generate a unique email
        unique_email = f"testuser_{int(time.time())}@example.com"
        email_field.send_keys(unique_email)

        company_field.send_keys("TestCorp")
        password_field.send_keys("test11")
        confirm_password_field.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        confirmation_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.result")))

        # Step 8: Verify that registration succeeded
        self.assertTrue(confirmation_message is not None, "Confirmation message is missing.")
        self.assertIn("Your registration completed", confirmation_message.text, "Registration did not succeed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()